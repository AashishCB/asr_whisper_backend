import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = RotatingFileHandler('../applog/{:%Y-%m-%d}.log'.format(datetime.utcnow()), maxBytes=20971520,
                                   backupCount=50)
file_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(file_handler)


class Tag:
    SPEECH_TO_TEXT = 'SPEECH_TO_TEXT'
    EXCEPTION = 'EXCEPTION'
    RESPONSE = 'RESPONSE'


class Log:

    @classmethod
    def e(cls, msg):
        logger.setLevel(logging.ERROR)
        logger.error(msg)

    @classmethod
    def d(cls, msg):
        logger.setLevel(logging.DEBUG)
        logger.debug(msg)

    @classmethod
    def i(cls, msg):
        logger.setLevel(logging.INFO)
        logger.info(msg)
