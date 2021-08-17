import pathlib
from os import path


PROJECT_PATH = pathlib.Path().resolve()
BANNER_FILE_PATH = path.join(PROJECT_PATH, 'resources', 'banner.txt')
SETTINGS_FILE_PATH = path.join(PROJECT_PATH, 'resources', 'settings.json')