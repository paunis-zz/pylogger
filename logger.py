#!/usr/bin/env python3

import logging as logthings
import os
import sys


def setup_logging():
    """Removes the default root handlers if any is set.
    Changes log level based on environment variable.

    :returns: the_logger
    :rtype: logging.Logger
    """
    level = environ.get('LOGLEVEL')

    if level is not None and isinstance(level, str):
        logthings.basicConfig(level=level.upper())
    else:
        logthings.basicConfig(level='INFO')

    root_logger = logthings.getLogger()
    for h in root_logger.handlers:
        root_logger.removeHandler(h)
    the_logger = logthings.getLogger(__name__)

    if not the_logger.handlers:
        formatter = logthings.Formatter(
            "[%(levelname)s] %(asctime)s, %(funcName)s, %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        handler = logthings.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        the_logger.addHandler(handler)

    return the_logger
