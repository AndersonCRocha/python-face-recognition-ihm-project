import json

import face_recognition

from src.constants import CONFIDENCE_LEVEL, SETTINGS_FILE_PATH, TIME_BETWEEN_PROCESSES_EXECUTION
from src.logger import Logger
from src.utils import get_random_encoded_photo_not_in, get_encoded_photo_by_name


class Condominium:
    def __init__(self, environment):
        Logger.info(self, 'Initializing condominium instance.')
        self.__environment = environment
        self.__load_settings()
        self.__prepare_environment()

        self.__recognized_people = []
        self.__tenants = []
        self.__visitors = []

    def __load_settings(self):
        Logger.info(self, f'Reading settings file in: {SETTINGS_FILE_PATH}.')
        with open(SETTINGS_FILE_PATH, 'r') as settings_file:
            self.settings = json.load(settings_file)
            Logger.info(self, f'Settings: {json.dumps(self.settings, indent=2)}')

    def __prepare_environment(self):
        self.__environment.add_process('recognize_people()', self.__recognize_people())
        self.__environment.add_process('classify_list()', self.__classify_recognized_people())
        self.__environment.add_process('unlock_to_tenants()', self.__unlock_to_tenants())
        self.__environment.add_process('unlock_to_visitors()', self.__unlock_to_visitors())
        self.__environment.add_process('people_leaves()', self.__people_leaves())

    def __recognize_people(self):
        while True:
            Logger.info(self, f'Recognizing person...')

            tenants = self.settings['tenants']
            random_encoded_photo = get_random_encoded_photo_not_in(self.__recognized_people)
            number_of_recognized_photos = 0

            for tenant in tenants:
                tenant_photos = tenant['photos']

                for photo in tenant_photos:
                    tenant_encoded_photo = get_encoded_photo_by_name(photo)

                    recognized = face_recognition.compare_faces([random_encoded_photo], tenant_encoded_photo)
                    if recognized:
                        number_of_recognized_photos += 1

                if (number_of_recognized_photos / len(tenant_photos)) > CONFIDENCE_LEVEL:
                    Logger.info(self, f'One person was recognized: {tenant["name"]}')

                    self.__recognized_people.append(tenant)

            yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION)

    def __classify_recognized_people(self):
        while True:
            print('__classify_list')
            yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION)

    def __unlock_to_tenants(self):
        while True:
            print('__unlock_to_tenants')
            yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION)

    def __unlock_to_visitors(self):
        while True:
            print('__unlock_to_visitors')
            yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION)

    def __people_leaves(self):
        while True:
            print('__people_leaves')
            yield self.__environment.timeout(TIME_BETWEEN_PROCESSES_EXECUTION)

    def __unlock_door(self):
        pass

    def __notify_tenant(self):
        pass

    def run_processes(self):
        self.__environment.run()
