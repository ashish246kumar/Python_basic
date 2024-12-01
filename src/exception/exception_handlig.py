# Importing the logging module to log error messages

import logging
# Using a try-except block to handle potential exceptions

try:
    x=10/0
except ZeroDivisionError as e:
    logging.error(e)


