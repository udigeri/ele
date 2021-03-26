from config import Config
from logger import EleLogger
from converter import Converter
from elevation import Elevation

class App(object):
    APP_INITIAL_MSG = "KST elevation profiler"

    def __init__(self, version, params):
        self.version = version
        print("{} {}".format(self.APP_INITIAL_MSG, self.version))
        self.config = Config(params = params)
        self.logger = EleLogger(self.config, version)
        self.logger.info(self.APP_INITIAL_MSG)

    def run(self):
        # cnv = Converter(self.config, self.logger)
        el = Elevation(self.config, self.logger)

    def finished(self):
        self.logger.info(self.APP_INITIAL_MSG + " finished")
