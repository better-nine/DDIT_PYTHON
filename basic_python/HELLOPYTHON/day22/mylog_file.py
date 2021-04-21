import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# 콘솔 출력을 지정합니다
ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)

# 파일 출력을 지정합니다.
fh = logging.FileHandler(filename="run.log")
#fh.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)


logger.critical("critical")
logger.error("error")
logger.warning("warning")
logger.info("info")
logger.debug("debug")