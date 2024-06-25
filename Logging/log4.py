#streamhandler
#filehandler
import logging

logger=logging.getLogger('sample-logger')  #log handler
logger.setLevel(logging.DEBUG)


#create a stream handler--> used for sending to terminal
sh=logging.StreamHandler()
sh.setLevel(logging.DEBUG)
#create a file handler--> used for sending to file
fh=logging.FileHandler('message-1.log', mode='w')
fh.setLevel(logging.DEBUG)

#format object
format=logging.Formatter("%(name)s %(levelname)s %(asctime)s %(message)s")

sh.setFormatter(format)
fh.setFormatter(format)

logger.addHandler(sh)
logger.addHandler(fh)

logger.debug("this is debug log")
logger.info("this is information log")
logger.warning("this is warning log")
logger.critical("this is a critical log")