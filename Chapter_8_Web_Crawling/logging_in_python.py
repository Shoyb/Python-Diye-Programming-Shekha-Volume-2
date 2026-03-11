import logging

logging.basicConfig(filename="test.log",filemode="w", level=logging.DEBUG,
                    format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

logging.info("This is info log.")
logging.debug("This is debug log.")
logging.warning("This is warning log.")
logging.error("This is error log.")
logging.critical("This is critical log.")
