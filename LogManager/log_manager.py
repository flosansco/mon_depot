import logging
from colorama import Fore, Style, init

# Initialize colorama (useful for Windows)
init(autoreset=True)

# Create a custom logging formatter with colors
class CustomFormatter(logging.Formatter):
    # Define color formats for different log levels
    FORMATS = {
        logging.DEBUG: Fore.BLUE + "%(levelname)s: %(message)s" + Style.RESET_ALL,
        logging.INFO: Fore.GREEN + "%(levelname)s: %(message)s" + Style.RESET_ALL,
        logging.WARNING: Fore.YELLOW + "%(levelname)s: %(message)s" + Style.RESET_ALL,
        logging.ERROR: Fore.RED + "%(levelname)s: %(message)s" + Style.RESET_ALL,
        logging.CRITICAL: Fore.RED + Style.BRIGHT + "%(levelname)s: %(message)s" + Style.RESET_ALL,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, "%(levelname)s: %(message)s")
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# Set up the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Apply the custom formatter to the handler
ch.setFormatter(CustomFormatter())

# Add the handler to the logger
logger.addHandler(ch)

# Example log messages
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
