import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger('sample-logger')  #log handler

logger.debug("this is debug log")
logger.info("this is information log")
logger.warning("this is warning log")
logger.critical("this is a critical log")