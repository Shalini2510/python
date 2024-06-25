import logging
logging.basicConfig(level=logging.WARNING)  #priority is set to WARNING so only warning and critical will run if we set to INFO then 
logger=logging.getLogger()                   # info,warning and critical will run 

logger.debug("this is debug log")
logger.info("this is information log")
logger.warning("this is warning log")
logger.critical("this is a critical log")