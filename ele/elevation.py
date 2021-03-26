class Elevation():
    def __init__(self, config, logger):
        self._convert_log_file(config, logger)

    def _convert_log_file(self, config, logger): 
        if self._is_config_file_prepared(config, logger) == True:
            src_file = getattr(config, "src_data_file")
            dst_file = getattr(config, "dst_data_file")
            try:
                logger.debug("Conversion Start")
                with open(src_file, 'r') as fr:
                    with open(dst_file, 'w') as fw:
                        for line in fr.readlines():
                            fw.write(line.upper())
                logger.debug("Conversion DONE")

            except IOError as err: 
                logger.error(err)
    
    def _is_config_file_prepared(self, config, logger):
        try:
            src_file = getattr(config, "src_data_file")
            dst_file = getattr(config, "dst_data_file")
            return True
        except AttributeError as err:
            logger.warning("Configuration file not correct check {} {}".format(getattr(config, "config_filepath"), err))
            return False