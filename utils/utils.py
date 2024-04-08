import logging


def get_logger():
    # logger instance 생성
    logger = logging.getLogger('logger')

    #formatter 생성
    formatter = logging.Formatter(fmt="(%(name)s) %(asctime)s [%(levelname)s] "
                                      "(%(filename)s:%(lineno)d) : %(message)s",
                                  datefmt="%Y-%m-%dT%H:%M:%S")

    #handler 생성
    streamHandler = logging.StreamHandler()
    #handler에 formatter 세팅
    streamHandler.setFormatter(formatter)


    if logger.hasHandlers():
        logger.handlers.clear()
    # logger instance에 handler 세팅
    logger.addHandler(streamHandler)

    # logger instance로 log 찍기
    logger.setLevel(logging.DEBUG)

    return logger
