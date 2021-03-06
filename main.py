from src.condominium import Condominium
from src.constants import BANNER_FILE_PATH
from src.environment import Environment
from src.logger import Logger
from src.utils import generate_log_filename

if __name__ == '__main__':
    try:
        Logger.debug = True
        Logger.filename = generate_log_filename()
        Logger.banner(BANNER_FILE_PATH)

        environment = Environment()
        condominium = Condominium(environment)

        condominium.run_processes()
    except RuntimeError as error:
        Logger.error(str(error))


