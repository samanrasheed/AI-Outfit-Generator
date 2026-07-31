import logging

#configure how logs look.
logging.basicConfig(
    level=logging.INFO, # Set the logging level to INFO(shows all messages at this level and above)
    format="%(asctime)s - %(levelname)s - %(message)s" #how the log messages will be displayed, including timestamp, log level, and message
)

logger = logging.getLogger(__name__) #creates a logger for this file and create logger object that can be used to log messages throughout the application. The __name__ argument ensures that the logger is named after the module in which it is used, making it easier to identify the source of log messages.