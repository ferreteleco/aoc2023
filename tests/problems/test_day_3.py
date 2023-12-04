"""
test_day_3.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 03/12/23 23:02:41.008000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from aoc2023.problems.day_3 import (
    Gear,
    Number,
    Symbol,
    compute_gear_ratios,
    compute_parts_sum,
    find_gears,
    find_part_numbers,
    parse_lines,
)


def test_find_adjacent_parts() -> None:
    """Test the function that obtains the part numbers from the input schematic, parsed line by
    line."""

    # Inputs
    rows = ["467..114+.", "...*......", "..35..633."]

    # Expected outputs
    expected_part_numbers = [467, 114, 35]

    # Element Under Test (EUT)
    computed_part_numbers = find_part_numbers(rows)

    # Checks
    assert len(expected_part_numbers) == len(computed_part_numbers)
    assert expected_part_numbers == computed_part_numbers


def test_find_adjacent_parts_longer_input() -> None:
    """Test the function that obtains the part numbers from the input schematic, parsed line by
    line from a longer input."""

    # Inputs
    rows = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    # Expected outputs
    expected_part_numbers = [467, 35, 633, 617, 592, 755, 664, 598]
    expected_sum = 4361

    # Element Under Test (EUT)
    computed_part_numbers = find_part_numbers(rows)

    # Checks
    assert len(expected_part_numbers) == len(computed_part_numbers)
    assert expected_part_numbers == computed_part_numbers
    assert sum(computed_part_numbers) == expected_sum


def test_compute_parts_sum() -> None:
    """Tests the part numbers sum function."""

    # Inputs
    part_numbers = [467, 114, 35]

    # Expected outputs
    expected_sum = 616

    # Element Under Test (EUT)
    computed_sum = compute_parts_sum(part_numbers)

    # Checks
    assert computed_sum == expected_sum


def test_number_class():
    """Test the implementation of the Number class."""

    # Inputs
    row = 0
    start = 2
    end = 4
    val = "22"

    # Expected outputs
    expected_val = 22
    expected_box = {
        (0, 1),
        (1, 2),
        (0, 4),
        (-1, 4),
        (-1, 1),
        (1, 1),
        (1, 4),
        (-1, 3),
        (-1, 2),
        (1, 3),
    }

    # Element Under Test (EUT)
    computed_number = Number(row, start, end, val)

    # Checks
    assert computed_number.value == expected_val
    assert computed_number.box == expected_box


def test_symbol_class():
    """Test the implementation of the Symbol class."""

    # Inputs
    row = 0
    col = 1
    symbol = "%"

    # Expected outputs
    expected_symb = "%"
    expected_pos = (0, 1)

    # Element Under Test (EUT)
    computed_symbol = Symbol(symbol, row, col)

    # Checks
    assert computed_symbol.symb == expected_symb
    assert computed_symbol.position == expected_pos


def test_parse_lines() -> None:
    """Test the function that parses line by line and creates the map of symbols and numbers."""

    # Inputs
    rows = ["467..114+.", "...*......"]

    # Expected outputs
    expected_numbers = [Number(0, 0, 3, "467"), Number(0, 5, 8, "114")]
    expected_symbols = [Symbol("+", 0, 8), Symbol("*", 1, 3)]

    # Element Under Test (EUT)
    computed_numbers, computed_symbols = parse_lines(rows)

    # Checks
    assert len(computed_numbers) == len(expected_numbers)
    assert len(computed_symbols) == len(expected_symbols)

    assert all(
        [
            exp.value == comp.value
            for exp, comp in zip(expected_numbers, computed_numbers)
        ]
    )
    assert all(
        [exp.symb == comp.symb for exp, comp in zip(expected_symbols, computed_symbols)]
    )


def test_gear_class():
    """Test the implementation of the Gear class."""

    # Inputs
    row = 0
    col = 1
    parts = [121, 221]

    # Expected outputs
    expected_symb = "*"
    expected_pos = (0, 1)
    expected_parts = [121, 221]

    # Element Under Test (EUT)
    computed_gear = Gear(row, col, parts)

    # Checks
    assert computed_gear.symb == expected_symb
    assert computed_gear.position == expected_pos
    assert computed_gear.parts == expected_parts


def test_filter_gears():
    """Test the implementation of the filter_gears static method."""

    # Inputs
    gears = [
        Gear(0, 1, [22, 11, 2, 3]),
        Gear(10, 1, [22, 11, 3]),
        Gear(20, 11, [22, 11]),
    ]

    # Expected outputs
    expected_valid_gears = [Gear(20, 11, [22, 11])]

    # Element Under Test (EUT)
    computed_valid_gears = Gear.filter_gears(gears)

    # Checks
    assert len(computed_valid_gears) == len(expected_valid_gears)
    for computed_gear, expected_gear in zip(computed_valid_gears, expected_valid_gears):
        assert computed_gear.position == expected_gear.position
        assert computed_gear.parts == expected_gear.parts


def test_find_gears() -> None:
    """Tests the function that finds gears in a given search space (parts and symbols)"""

    # Inputs
    parts = [Number(0, 0, 3, "467"), Number(0, 5, 8, "114"), Number(2, 2, 4, "35")]
    symbols = [Symbol("+", 0, 8), Symbol("*", 1, 3)]

    # Expected outputs
    expected_gears = [Gear(1, 3, [467, 35])]

    # Element Under Test (EUT)
    computed_gears = find_gears(parts, symbols)

    # Checks
    assert len(computed_gears) == len(expected_gears)
    for computed_gear, expected_gear in zip(computed_gears, expected_gears):
        assert computed_gear.position == expected_gear.position
        assert computed_gear.parts == expected_gear.parts


def test_compute_gear_ratios() -> None:
    """Test the function that compute gear ratios."""

    # Inputs
    gears = [
        Gear(0, 1, [22, 11]),
        Gear(10, 1, [21, 3]),
        Gear(20, 11, [222, 511]),
    ]

    # Expected outputs
    expected_gear_ratios = [242, 63, 113442]

    # Element Under Test (EUT)
    computed_gear_ratios = compute_gear_ratios(gears)

    # Checks
    assert len(computed_gear_ratios) == len(expected_gear_ratios)
    assert computed_gear_ratios == expected_gear_ratios
