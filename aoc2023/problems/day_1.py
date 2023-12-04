"""
day_1.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 01/12/23 15:58:04.291000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from __future__ import annotations

from typing import Literal

from loguru import logger as LOG
from regex import findall

WORD_TO_DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def compute_calibration_numbers(
    list_of_lines: list[str],
    pattern: Literal["digits"] | Literal["alpha"] = "digits",
) -> tuple[list[int], int]:
    """Computes the calibration numbers needed by the elves.

    Mode "digits":
        - On each line, the calibration value can be found by combining the first digit and the last
        digit (in that order) to form a single two-digit number.
    Mode "alpha":
        - Some of the digits are actually spelled out with letters: one, two, three, four, five,
        six, seven, eight, and nine also count as valid "digits".

    The additional checksum is simply the sum of all calibration values.

    Args:
        list_of_lines (list[str]): List of lines to be processed.
        pattern (Literal["digits"] | Literal["alpha"], optional): Flag indicating the computation
        mode for the calibration list. Defaults to "digits".


    Returns:
        Tuple[list[int], int]: List of calibration values and checksum of them.
    """

    LOG.info("Computing calibration values for {} input lines", len(list_of_lines))

    calibration_lines = []

    match pattern:
        case "digits":
            re_pattern = r"\d"
        case "alpha":
            word_set = [
                "one",
                "two",
                "three",
                "four",
                "five",
                "six",
                "seven",
                "eight",
                "nine",
            ]
            re_pattern = r"(?i:\d|" + r"|".join(word_set) + r")"

    for line in list_of_lines:
        matches = findall(re_pattern, line, overlapped=True)
        if matches:
            n0 = (
                matches[0]
                if matches[0].isdigit()
                else WORD_TO_DIGIT[matches[0].lower()]
            )
            n1 = (
                matches[-1]
                if matches[-1].isdigit()
                else WORD_TO_DIGIT[matches[-1].lower()]
            )

            calibration_lines.append(int(n0 + n1))

    checksum = sum(calibration_lines)

    return calibration_lines, checksum
