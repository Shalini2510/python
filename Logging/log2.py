import logging
logging.basicConfig(level=logging.DEBUG, filename='message.log', filemode='w')
logger=logging.getLogger()

logger.debug("this is debug log")
logger.info("this is information log")
logger.warning("this is warning log")
logger.critical("this is a critical log")