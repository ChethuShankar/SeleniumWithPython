import logging


class LoggerDemo:
    def sample_logger(self):
        # create Logger
        logger = logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.DEBUG)
        # create console handler or file handler and set the log level
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("demologs.log")
        # create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - % (name)s-% (message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter1 = logging.Formatter('% (asctime)s - %(levelname)s - % (name)s: % (message)s')
        # add formatter to console or file handler
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter1)
        # add console handler to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        # application code Log messages
        logger.debug("debug log statement")
        logger.error("error statement")
        logger.info("info statement")
        logger.critical("critical statement")


ld = LoggerDemo()
ld.sample_logger()
