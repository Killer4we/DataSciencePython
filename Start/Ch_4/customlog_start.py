# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
fmtstring = "User: %(user)s : %(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s"
extradata = {
    "user":"Abhinav Tomar"
}

def anotherFunc():
    logging.debug("This is my new message from a random function",extra=extradata)

# set the output file and debug level, and
# TODO: use a custom formatting specification
dateformat = "%m/%d/%Y %I:%M:%S %p"
logging.basicConfig(filename="output2.log",
                    filemode="w",
                    level=logging.DEBUG,
                    format=fmtstring,
                    datefmt=dateformat)

logging.info("This is an info-level log message",extra=extradata)
logging.warning("This is a warning-level message",extra=extradata)
anotherFunc()
