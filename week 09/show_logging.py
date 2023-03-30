# show_logging.py
# Author: Rachel King

import logging
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename= "debugging.log",
    filemode="a",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d')


name = 'Joe'

logging.error("This is an error")
logging.critical("hiya")
logging.warning("dont know %s", name)
logging.info("still going")
logging.debug("and so is this")