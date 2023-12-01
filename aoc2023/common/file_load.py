"""
file_load.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 01/12/23 15:34:08.631000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from pathlib import Path

from loguru import logger as LOG


def load_input_file(file: Path) -> list[str]:
    """Loads and input file and returns all its lines (stripped).

    Args:
        file (Path): Path to the file to be read.

    Returns:
        list[str]: List of processed lines.
    """

    lines = []

    try:
        LOG.info("Reading input file")
        with file.open("r", encoding="UTF-8") as fd:
            for line in fd:
                lines.append(line.strip())

    except FileNotFoundError as err:
        LOG.critical("File does not exist: {} ({})", str(file), err.args)
    except PermissionError as err:
        LOG.critical("Permission denied for file: {} ({})", str(file), err.args)
    except IOError as err:
        LOG.critical("IOError happened in file {}: ({})", str(file), err.args)

    return lines
