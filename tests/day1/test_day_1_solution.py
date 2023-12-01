"""
test_day_1_solution.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 01/12/23 15:29:35.244000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""


from aoc2023.day1.problems import compute_calibration_numbers


def test_day_1_calibration_report() -> None:
    """Test the solution of the first problem of AoC's 1st day."""

    # Inputs
    in_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

    # Expected outputs
    expected_values = [12, 38, 15, 77]
    expected_checksum = 142

    # Element Under Test (EUT)
    computed_list, computed_checksum = compute_calibration_numbers(in_data, "digits")

    # Checks
    assert len(computed_list) == len(expected_values)
    assert computed_list == expected_values
    assert computed_checksum == expected_checksum


def test_day_1_calibration_report_adjacent() -> None:
    """Test the solution of the first problem of AoC's 1st day, testing for adjacent digits."""

    # Inputs
    in_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet", "33fkrl1"]

    # Expected outputs
    expected_values = [12, 38, 15, 77, 31]
    expected_checksum = 173

    # Element Under Test (EUT)
    computed_list, computed_checksum = compute_calibration_numbers(in_data, "digits")

    # Checks
    assert len(computed_list) == len(expected_values)
    assert computed_list == expected_values
    assert computed_checksum == expected_checksum


def test_day_1_calibration_report_alphanumeric() -> None:
    """Test the solution of the second problem of AoC's 1st day."""

    # Inputs
    in_data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
        "33fkrl1",
    ]

    # Expected outputs
    expected_values = [29, 83, 13, 24, 42, 14, 76, 31]
    expected_checksum = 312

    # Element Under Test (EUT)
    computed_list, computed_checksum = compute_calibration_numbers(in_data, "alpha")

    # Checks
    assert len(computed_list) == len(expected_values)
    assert computed_list == expected_values
    assert computed_checksum == expected_checksum
