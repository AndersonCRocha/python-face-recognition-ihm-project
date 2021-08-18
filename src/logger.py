from os import path
from time import localtime, strftime


class Logger:
    debug = False
    filename = 'log.txt'

    @classmethod
    def info(cls, clazz, message):
        datetime = strftime("[%d-%m-%Y %H:%M:%S]", localtime())
        class_information = f'Class: {clazz.__class__.__name__}' if clazz else ''
        cls.__log(f'{datetime} - {class_information} - {message}\n')

    @classmethod
    def error(cls, error):
        cls.__log(f'ERROR::: {error}')

    @classmethod
    def banner(cls, banner_path):
        with open(banner_path, 'r') as banner:
            cls.__log(f'{banner.read()}\n')

    @classmethod
    def __log(cls, message):
        log_file_path = path.join('.', 'logs', cls.filename)
        with open(log_file_path, 'a') as log_file:
            log_file.write(message)
            if cls.debug:
                print(message)
