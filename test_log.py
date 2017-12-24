import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()

#定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
rtHandler = RotatingFileHandler('.\\log\\log.txt', maxBytes=10*1024*1024,backupCount=5)
rtHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(message)s')
rtHandler.setFormatter(formatter)
logger.addHandler(rtHandler)

logger.error("test")