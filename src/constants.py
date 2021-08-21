import pathlib
from os import path

CONFIDENCE_LEVEL = 0.7

TIME_BETWEEN_PROCESSES_EXECUTION = 20

PROJECT_PATH = pathlib.Path().resolve()
RESOURCES_PATH = path.join(PROJECT_PATH, 'resources')
PHOTOS_PATH = path.join(RESOURCES_PATH, 'photos')
BANNER_FILE_PATH = path.join(RESOURCES_PATH, 'banner.txt')
SETTINGS_FILE_PATH = path.join(RESOURCES_PATH, 'settings.json')


