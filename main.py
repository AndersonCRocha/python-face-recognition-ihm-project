from src.environment import Environment
from src.logger import Logger

if __name__ == '__main__':
    Logger.debug = True
    Logger.banner('./resources/banner.txt')
    environment = Environment()
    environment.run()
