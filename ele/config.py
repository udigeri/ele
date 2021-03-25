import yaml
import os

class Config():
    def __init__(self, params=None):
        self.params = params
        self.config_filepath = params.config_file
        self.environment = params.ele_env

        self._load_config_file(self.config_filepath)

        if not hasattr(self, 'log_level'): 
            setattr(self, 'log_level', 'info')
        if not hasattr(self, 'log_file'): 
            setattr(self, 'log_file', './ele.log ')
        # print("log_level => {}".format(getattr(self, "log_level")))
        # print("log_file  => {}".format(getattr(self, "log_file")))

    def _parse_section(self, key, value):
        if type(value) == dict:
            for subkey,subvalue in value.items():
                self._parse_section(key + "_" + subkey, subvalue)
        else:
            setattr(self, key, value)
 
    def _load_config_file(self, filepath):
        with open(filepath, 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)[self.environment]
        for key,value in cfg.items():
            self._parse_section(key,value)
 