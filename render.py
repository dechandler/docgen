#!/usr/bin/env python3.13
"""


"""
import os
import sys

from docgen import (DocgenConfig, DocgenApi)

# from .exceptions import ()


def _main():

    config = DocgenConfig("docgen-readme")
    log = config.log

    log.info("Starting Resume Renderer")
    log.debug(f"  PID: {os.getpid()}")
    log.debug(f"  Args: {sys.argv[1:]}")

    try:
        data_name, template_filename = [*sys.argv[1:]]
    except ValueError:
        log.error("Wrong number of args")
        sys.exit(1)

    api = DocgenApi()


def main():

    try:
        _main()
    except (
        KeyboardInterrupt
    ) as e:
        print(f"Exiting due to {e.__class__}: {str(e)}")
