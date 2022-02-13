#!/usr/bin/env python3
"""Console script for test_repo."""

from logging import getLogger
from logging.config import fileConfig
from os import makedirs, utime
from os.path import abspath, dirname, exists, join
from platform import machine, python_version, system
from sys import exit


def main():
    """Main"""
    pass


if __name__ == "__main__":
    __loggername__ = "test_repo"
    fileConfig(fname={}).format(join(dirname(dirname(abspath(__file__))), "conf"))
    log = getLogger(__loggername__)
    log.debug(
        "%s-%s running on Python version: %s-%s on %s",
        __loggername__,
        "0.1.0",
        python_version(),
        machine(),
        system(),
    )
    log.debug(
        "Configuration settings:\n\n \
Approot: %s |\n \
Logconfig file: %s |\n \
Config file: %s |\n",
        parser.app_root,
        parser.default_logconf,
        parser.config_file,
    )

    main()
