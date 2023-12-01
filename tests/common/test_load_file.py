"""
test_load_file.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 01/12/23 15:30:27.119000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from pathlib import Path

from aoc2023.common.file_load import load_input_file


def test_load_input_file_exist() -> None:
    """Checks that a given input file can be read and processed."""

    # Inputs
    in_file = Path("data/inputs/input_demo_loadfile.txt")

    # Expected outputs
    expected_lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

    # Element Under Test (EUT)
    read_lines = load_input_file(in_file)

    # Checks
    assert len(read_lines) == len(expected_lines)
    assert read_lines == expected_lines


def test_load_input_file_nonexistent() -> None:
    """Checks that a given input file which is nonexistent returns an empty list."""

    # Inputs
    in_file = Path("data/inputs/input_demo_loadfile_fake.txt")

    # Element Under Test (EUT)
    expected = load_input_file(in_file)

    # Checks
    assert len(expected) == 0
