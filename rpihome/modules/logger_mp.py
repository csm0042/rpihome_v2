import logging


def listener_configurer(name, debug_logfile, info_logfile):
    logger = logging.getLogger(name)
    logger.handlers = []
    # Create desired handlers
    debug_handler = logging.handlers.TimedRotatingFileHandler(debug_logfile, when="h", interval=1, backupCount=24, encoding=None, delay=False, utc=False, atTime=None)
    info_handler = logging.handlers.TimedRotatingFileHandler(info_logfile, when="h", interval=1, backupCount=24, encoding=None, delay=False, utc=False, atTime=None)
    console_handler = logging.StreamHandler()
    # Create individual formats for each handler
    debug_formatter = logging.Formatter('%(processName)-16s,  %(asctime)-24s,  %(levelname)-8s, %(message)s')
    info_formatter = logging.Formatter('%(processName)-16s,  %(asctime)-24s,  %(levelname)-8s, %(message)s')    
    console_formatter = logging.Formatter('%(processName)-16s,  %(asctime)-24s,  %(levelname)-8s, %(message)s')
    # Set formatting options for each handler
    debug_handler.setFormatter(debug_formatter)
    info_handler.setFormatter(info_formatter)
    console_handler.setFormatter(console_formatter)
    # Set logging levels for each handler
    debug_handler.setLevel(logging.DEBUG)
    info_handler.setLevel(logging.INFO)
    console_handler.setLevel(logging.INFO)
    # Add handlers to root logger
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(console_handler)
    return logger



def worker_configurer(name, queue):
    h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
    logger = logging.getLogger(name)
    logger.handlers = []
    logger.addHandler(h)
    # send all messages, for demo; no other level or filter logic applied.
    logger.setLevel(logging.DEBUG)
    return logger    