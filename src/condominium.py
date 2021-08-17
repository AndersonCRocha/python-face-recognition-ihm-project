from src.logger import Logger


class Condominium:
    def __init__(self, environment):
        Logger.info(self, 'Initializing condominium instance.')
        self.__environment = environment
        self.__load_settings()
        self.__prepare_environment()

        self.__recognized_persons = []
        self.__tenants = []
        self.__visitors = []

    def __load_settings(self):
        pass

    def __prepare_environment(self):
        self.__environment.add_process('recognize_people()', self.__recognize_people())
        self.__environment.add_process('classify_list()', self.__classify_list())

    def __recognize_people(self):
        while True:
            print('__recognize_people')
            yield self.__environment.timeout(10)

    def __classify_recognized_people(self):
        while True:
            print('__classify_list')
            yield self.__environment.timeout(20)

    def __unlock_door(self):
        pass

    def __notify_tenant(self):
        pass

    def run_processes(self):
        self.__environment.run()
