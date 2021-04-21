import logging


mylogger = logging.getLogger("my")
mylogger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)
mylogger.addHandler(stream_hander)

file_handler = logging.FileHandler('my.log')
file_handler.setFormatter(formatter)
mylogger.addHandler(file_handler)

mylogger.debug("i am debug")
mylogger.info("i am info")
mylogger.warning("i am warning")
mylogger.error("i am error")
mylogger.fatal("i am fatal")
