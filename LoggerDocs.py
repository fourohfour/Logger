from logger import *

### Documentation - Logger ###

# Create a new logger
#  The first argument, False:
#  This specifies if new logs should be automatically printed
#
#  The second argument, "LOG START"
#  This is the header; the first line to be printed to the log
#
#  The third optional argument (not shown here)
#  This specifies how the time is rendered by the logger
#  This should be a string, and can contain the following
#  %y - Year; %m - Month; %d - Day;
#  %H - Hour; %M - Minute; %S - Second;

logger = Logger(False, "LOG START")

# Add a log to the logger
#  The arguments specify the type of log and the text to be logged
#  More Log Types can be added in the LogType enum.

logger.log(LogType.INFO, "Test Log")


## Main Methods

# This prints all new logs and moves the pointer forward to the current one
#  New refers to any logs since the last time the logs were read
#  The position of New in the list is held by a pointer variable
#  The position of the pointer is not changed by autoprint

logger.printNew()

# This method prints everything regardless of the pointer position

logger.printAll()


## Pointer Methods

logger.resetPointer() # Sets Pointer to 0

logger.getPointer() # Gets the Pointer value

logger.setPointer(3) # Sets the Pointer value
                     # If the argument is < 0 it becomes zero
                     # If the argument is > log length it becomes log length

logger.incrementPointer() # Adds 1 to the Pointer
logger.incrementPointer(3)# Optional Argument
                          # Prevents Illegal Values

logger.decrementPointer() # Takes 1 from the Pointer
logger.decrementPointer(3)# Optional Argument
                          # Prevents Illegal Values


## Misc. Methods

logger.getNew() # Gets new values and returns as list; moves pointer

logger.getAll() # Gets all values and returns as list
