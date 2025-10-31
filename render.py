#!/usr/bin/env python3.13
"""


"""
import os
import sys

from docgen import (DocgenConfig, DocgenApi)

# from .exceptions import ()


log = logging.getLogger("docgen-readme-gen")


def _main():

    try:
        data_name, tmpl_name = [*sys.argv[1:]]
    except ValueError:
        log.error("Wrong number of args")
        sys.exit(1)

    config = DocgenConfig(log)

    log.info("Starting Docgen README update")
    log.debug(f"  PID: {os.getpid()}")
    log.debug(f"  Args: {sys.argv[1:]}")


    api = DocgenApi(self.config)
    api.render(tmpl_name, data_name, f"{data_name}-{tmpl_name}")


def main():

    try:
        _main()
    except (
        KeyboardInterrupt
    ) as e:
        print(f"Exiting due to {e.__class__}: {str(e)}")
