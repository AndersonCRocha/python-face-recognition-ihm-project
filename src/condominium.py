import json
import random

import face_recognition

from src.constants import CONFIDENCE_LEVEL, PROBABILITY_OF_A_PERSON_LEAVING, SETTINGS_FILE_PATH, \
    TIME_BETWEEN_PROCESSES_EXECUTION
from src.logger import Logger
from src.utils import get_random_encoded_photo, get_encoded_photo_by_name


class Condominium:
    def __init__(self, environment):
        Logger.info(self, 'Initializing condominium instance.')
        self.__environment = environment
        self.__load_settings()
        self.__prepare_environment()

        self.__recognized_people = []
        self.__waiting_tenants = []
        self.__waiting_visitors = []
        self.__tenants_in = []
        self.__visitors_in = []

    def __load_settings(self):
        Logger.info(self, f'Reading settings file in: {SETTINGS_FILE_PATH}.')
        with open(SETTINGS_FILE_PATH, 'r') as settings_file:
            self.__settings = json.load(settings_file)
            Logger.info(self, f'Settings: {json.dumps(self.__settings, indent=2)}')

    def __prepare_environment(self):
        self.__environment.add_process('recognize_people()', self.__recognize_people())
        self.__environment.add_process('classify_list()', self.__classify_recognized_people())
        self.__environment.add_process('unlock_to_tenants()', self.__unlock_to_tenants())
        self.__environment.add_process('unlock_to_visitors()', self.__unlock_to_visitors())
        self.__environment.add_process('people_leaves()', self.__people_leaves())

    def __recognize_people(self):
        while True:
            people = self.__get_all_registered_people()
            random_encoded_photo = get_random_encoded_photo()
            number_of_recognized_photos = 0

            for person in people:
                person_photos = person['photos']

                for photo in person_photos:
                    person_encoded_photo = get_encoded_photo_by_name(photo)

                    recognized = face_recognition.compare_faces([random_encoded_photo], person_encoded_photo)[0]
                    if recognized:
                        number_of_recognized_photos += 1

                recognition_confidence = (number_of_recognized_photos / len(person_photos)) > CONFIDENCE_LEVEL

                if recognition_confidence > CONFIDENCE_LEVEL \
                        and person not in self.__waiting_tenants \
                        and person not in self.__waiting_visitors\
                        and person not in self.__tenants_in \
                        and person not in self.__visitors_in:
                    Logger.info(self, f'One person was recognized: {person["name"]}')
                    self.__recognized_people.append(person)

                    yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION * 2)
                else:
                    Logger.info(self, 'Person not registered in allowed people list')

                    yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION)

    def __classify_recognized_people(self):
        all_registered_tenants = self.__get_all_registered_people(include_visitors=False)

        while True:
            number_of_recognized_people = len(self.__recognized_people)

            for person in self.__recognized_people:
                if person in all_registered_tenants:
                    Logger.info(self, f'{person["name"]} is a tenant.')
                    self.__waiting_tenants.append(person)
                else:
                    Logger.info(self, f'{person["name"]} is a visitor.')
                    self.__waiting_visitors.append(person)

                self.__recognized_people.remove(person)

            timeout = TIME_BETWEEN_PROCESSES_EXECUTION \
                if number_of_recognized_people == 0 \
                else TIME_BETWEEN_PROCESSES_EXECUTION * number_of_recognized_people

            yield self.__environment.timeout(timeout)

    def __unlock_to_tenants(self):
        while True:
            number_of_waiting_tenants = len(self.__waiting_tenants)

            for tenant in self.__waiting_tenants:
                Logger.info(self, f'Tenant "{tenant["name"]}" is allowed in.')
                self.__tenants_in.append(tenant)
                self.__waiting_tenants.remove(tenant)

            timeout = TIME_BETWEEN_PROCESSES_EXECUTION \
                if number_of_waiting_tenants == 0 \
                else TIME_BETWEEN_PROCESSES_EXECUTION * number_of_waiting_tenants

            yield self.__environment.timeout(timeout)

    def __unlock_to_visitors(self):
        all_registered_tenants = self.__get_all_registered_people(include_visitors=False)

        while True:
            number_of_waiting_visitors = len(self.__waiting_visitors)

            for visitor in self.__waiting_visitors:
                for tenant in all_registered_tenants:
                    if visitor in tenant['visitors']:
                        Logger.info(self, f'Calling visitor notification service for tenant "{tenant["name"]}".')
                        break

                self.__visitors_in.append(visitor)
                self.__waiting_visitors.remove(visitor)
                Logger.info(self, f'Visitor "{visitor["name"]}" is allowed in.')

            timeout = TIME_BETWEEN_PROCESSES_EXECUTION \
                if number_of_waiting_visitors == 0 \
                else TIME_BETWEEN_PROCESSES_EXECUTION * number_of_waiting_visitors

            yield self.__environment.timeout(timeout)

    def __people_leaves(self):
        while True:
            if random.randint(1, 100) <= PROBABILITY_OF_A_PERSON_LEAVING:
                random_choice = random.choice(['visitor', 'tenant'])

                if random_choice == 'visitor' and len(self.__visitors_in) > 0:
                    random_visitor = random.choice(self.__visitors_in)
                    self.__visitors_in.remove(random_visitor)
                    Logger.info(self, f'Visitor "{random_visitor["name"]}" is leaving the condominium: ')
                elif len(self.__tenants_in) > 0:
                    random_tenant = random.choice(self.__tenants_in)
                    self.__tenants_in.remove(random_tenant)
                    Logger.info(self, f'Tenant "{random_tenant["name"]}" is leaving the condominium: ')

                yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION * 4)
            else:
                yield self.__environment.timeout(1)

    def __get_all_registered_people(self, include_tenants=True, include_visitors=True):
        people = []

        for tenant in self.__settings['tenants']:
            if include_tenants:
                people.append(tenant)

            if include_visitors:
                for visitor in tenant['visitors']:
                    people.append(visitor)

        return people

    def run_processes(self):
        self.__environment.run()
