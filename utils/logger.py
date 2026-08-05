import logging

#configure how logs look.
logging.basicConfig(
    level=logging.INFO, # Set the logging level to INFO(shows all messages at this level and above)
    format="%(asctime)s - %(levelname)s - %(message)s" #how the log messages will be displayed, including timestamp, log level, and message
)

logger = logging.getLogger(__name__) ## Create a module-specific logger.