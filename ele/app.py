from config import Config
from logger import EleLogger
from elevation import Elevation

class App(object):
    APP_INITAL_MSG = "KST elevation profiler"

    def __init__(self, version, params):
        self.version = version
        print("{} {}".format(self.APP_INITAL_MSG, self.version))
        self.config = Config(params = params)
        self.logger = EleLogger(self.config, version)
        self.logger.info(self.APP_INITAL_MSG)
        # self.logger.debug(self.APP_INITAL_MSG)
        # self.logger.warn(self.APP_INITAL_MSG)
        # self.logger.error(self.APP_INITAL_MSG)
        # self.logger.critical(self.APP_INITAL_MSG)

    def run(self):
        el = Elevation(self.config, self.logger)
