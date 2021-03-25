import logging
import os

class EleLogger(logging.Logger):
    LOG_FORMATTER = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  
    def __init__(self, config, version):
        if not os.path.exists(os.path.dirname(config.log_file)):
            os.makedirs(os.path.dirname(config.log_file))

        logging.Logger.__init__(self, name="ele " + version + "")
        self.formatter = logging.Formatter(self.LOG_FORMATTER)
        self.setLevel(config.log_level.upper())
        self.propagate = False
        handler = logging.FileHandler(config.log_file)
        handler.setFormatter(self.formatter)
        self.addHandler(handler) 