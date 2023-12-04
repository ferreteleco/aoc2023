"""
day_3.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 03/12/23 23:06:28.175000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from __future__ import annotations
from functools import reduce
from loguru import logger as LOG
from regex import compile as regex_compile


class Number:
    """Simple class that defines a number (multi-char) and its adjacent cells inside a matrix
    (text).

    Attributes:
        value (int): Number value.
        box (set[tuple[int, int]]): Set of coordinates of the neighbouring cells.
    """

    def __init__(self, row: int, start: int, end: int, val: str):
        """Creates a new number instance.

        Args:
            row (int): Row of the number inside the matrix.
            start (int): Starting position (col) of the number inside the matrix.
            end (int): Ending position (exclusive) of the number inside the matrix.
            val (str): Value of the number, string encoded.
        """

        self.value = int(val)
        adj = {(row, start - 1), (row, end)}
        for c in range(start - 1, end + 1):
            adj.add((row + 1, c))
            adj.add((row - 1, c))
        self.box = adj


class Symbol:
    """Simple class that defines a symbol (single character) and its position within a text matrix.

    Attributes:
        symb (str): Number value.
        position (tuple[int, int]): Coordinates of the symbol within the matrix.
    """

    def __init__(self, symbol: str, row: int, col: int):
        """Creates a new symbol instance.

        Args:
            symbol (str): Actual symbol value (single char).
            row (int): Row where the symbol is located within the matrix.
            col (int): Column where the symbol is located within the matrix.
        """

        self.symb = symbol
        self.position = (row, col)


class Gear(Symbol):
    """Special symbol indicating a gear if certain conditions are met:

    - Symbol is '*'.
    - Symbol has exactly two adjacent parts.

    The filter_gears static method provides help to filter out Gears which not met the second
    condition from an input list.

    Attributes:
        parts (list[int]): List of adjacent parts. It must have length 2 for the gear to be valid.
    """

    def __init__(self, row: int, col: int, parts: list[int] | None = None):
        super().__init__("*", row, col)
        self.parts = parts if parts else []

    @staticmethod
    def filter_gears(gears: list["Gear"]) -> list["Gear"]:
        return [gear for gear in gears if len(gear.parts) == 2]


def parse_lines(rows: list[str]) -> tuple[list[Number], list[Symbol]]:
    """Parses the input lines classifying symbols and numbers and tagging the neighbouring cells of
    the latter.

    Args:
        rows (list[str]): List of rows of the text matrix, string encoded.

    Returns:
        tuple[list[Number], list[Symbol]]: _description_
    """

    pattern = r"(?P<number>\d+)|(?P<symbol>[^\d.])"
    regex = regex_compile(pattern)

    numbers = []
    symbols = []

    for row, line in enumerate(rows):
        for m in regex.finditer(line):
            number, symbol = m.groups()
            col = m.start()
            if number:
                numbers.append(Number(row, col, m.end(), number))
            elif symbol:
                symbols.append(Symbol(symbol, row, col))

    return numbers, symbols


def find_part_numbers(rows: list[str]) -> list[int]:
    """This function tries to find suitable part numbers in a list of strings representing input
    lines.

    Any number adjacent to a symbol, even diagonally, is a "part number" and should be included,
    noting that dots does not count as symbols.

    Args:
        rows (list[str]): List of input rows from the schematic.

    Returns:
        list[int]: List of valid part numbers.
    """

    parts, symbols = parse_lines(rows)
    symbol_locations = set([symbol.position for symbol in symbols])
    parts = [n.value for n in parts if symbol_locations & n.box]
    return parts


def compute_parts_sum(part_numbers: list[int]) -> int:
    """Computes the sum of a list of part numbers.

    Args:
        part_numbers (list[int]): List of received part numbers.

    Returns:
        int: Sum of the part numbers.
    """

    LOG.trace("Computing part number summatory")

    return sum(part_numbers)


def find_gears(parts: list[Number], symbols: list[Symbol]) -> list[Gear]:
    """Searches for gears in the found symbols.

    A gear is defined as a '*' symbol with exactly two adjacent parts.

    The provided static method is useful for filtering a list of candidate gears ('*' symbols) and
    ensuring the second condition is met.

    Args:
        parts (list[Number]): List of input part numbers.
        symbols (list[Symbol]): List of symbols.

    Returns:
        list[Gear]: List of valid gears.
    """

    candidate_gears = [
        Gear(symbol.position[0], symbol.position[1])
        for symbol in symbols
        if symbol.symb == "*"
    ]

    for part in parts:
        for coords in part.box:
            if gear := next(
                (gear for gear in candidate_gears if gear.position == coords), None
            ):
                gear.parts.append(part.value)

    gears = Gear.filter_gears(candidate_gears)

    return gears


def compute_gear_ratios(gears: list[Gear]) -> list[int]:
    """Computes the gear ratios for a list of input gears.

    Args:
        gears (list[Gear]): List of input gears.

    Returns:
        list[int]: List of gear ratios for each input gear.
    """

    gear_ratios = []
    for gear in gears:
        ratio = reduce((lambda x, y: x * y), gear.parts)
        gear_ratios.append(ratio)

    return gear_ratios
