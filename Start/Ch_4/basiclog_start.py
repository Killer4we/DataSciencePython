# demonstrate the logging api in Python

# TODO: use the built-in logging module

import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG,filemode="a",filename="output.log")
# TODO: Try out each of the log levels

logging.debug("debug level")
logging.info("info level")
logging.warning("warning level")
logging.error("error level")
logging.critical("critical level")

# TODO: Output formatted strings to the log
name = "Abhinav"
age = 20
# I am using formatted strings here
logging.info(f"Here's a string {name} and here's an integer {age}")