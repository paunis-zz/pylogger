#!/usr/bin/env python3

import logging
import os
import sys


def setup_logging(log_file=None):
    logger = logging.getLogger()
    for h in logger.handlers:
        logger.removeHandler(h)
    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s, %(funcName)s, %(message)s", "%Y-%m-%d %H:%M:%S")
    handler = logging.FileHandler(
        log_file, 'a') if log_file is not None else logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.raiseException = True
    try:
        LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
        logger.basicConfig(level=LOGLEVEL)
    except:
        logger.setLevel(logging.INFO)
    return logger
