#log --  Logging is a means of tracking events that happen when some software runs. 
#Logging is important for software developing, debugging, and running. 
#If you don’t have any logging record and your program crashes, there are very few chances that you detect the cause of the problem.
# And if you detect the cause, it will consume a lot of time. With logging, you can leave a trail of breadcrumbs so that if something 
#goes wrong, we can determine the cause of the problem. 

#import logging-- module used for generating logs

#logging levels :
#debug---It is a level with lowest priority
#       These are used to give Detailed information, typically of interest only when diagnosing problems.

#info-- These are used to confirm that things are working as expected.

#warning-- These are used as an indication that something unexpected happened, or is indicative of some problem in the near future.

#error--This tells that due to a more serious problem, the software has not been able to perform some function.

#critcal -- It is a level with highest priority.
#           This tells serious error, indicating that the program itself may be unable to continue running


import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()

logger.debug("this is debug log")
logger.info("this is information log")
logger.warning("this is warning log")
logger.critical("this is a critical log")