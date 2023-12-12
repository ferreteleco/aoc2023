"""
test_day_5.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 07/12/23 14:33:28.245000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""


from aoc2023.problems.day_5 import (
    expand_seeds_list,
    find_location_for_initial_seed,
    initialize_dicts,
    parse_lines,
    solve_part_1,
    solve_part_2,
)


def test_initialize_dicts() -> None:
    # Expected outputs
    # pylint: disable=duplicate-code
    expected_dict = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    # Element Under Test (EUT)

    computed_dict = initialize_dicts()

    # Checks
    assert len(computed_dict) == len(expected_dict)
    assert computed_dict == expected_dict


def test_parse_lines() -> None:
    # Inputs
    input_lines = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]

    # Expected outputs
    expected_seeds = [79, 14, 55, 13]
    expected_maps = {
        "seed-to-soil": [
            (range(98, 100), range(50, 52)),
            (range(50, 98), range(52, 100)),
        ],
        "soil-to-fertilizer": [
            (range(15, 52), range(0, 37)),
            (range(52, 54), range(37, 39)),
            (range(0, 15), range(39, 54)),
        ],
        "fertilizer-to-water": [
            (range(53, 61), range(49, 57)),
            (range(11, 53), range(0, 42)),
            (range(0, 7), range(42, 49)),
            (range(7, 11), range(57, 61)),
        ],
        "water-to-light": [
            (range(18, 25), range(88, 95)),
            (range(25, 95), range(18, 88)),
        ],
        "light-to-temperature": [
            (range(77, 100), range(45, 68)),
            (range(45, 64), range(81, 100)),
            (range(64, 77), range(68, 81)),
        ],
        "temperature-to-humidity": [
            (range(69, 70), range(0, 1)),
            (range(0, 69), range(1, 70)),
        ],
        "humidity-to-location": [
            (range(56, 93), range(60, 97)),
            (range(93, 97), range(56, 60)),
        ],
    }

    # Element Under Test (EUT)
    computed_seeds, computed_maps = parse_lines(input_lines)

    # Checks
    assert len(computed_seeds) == len(expected_seeds)
    assert computed_seeds == expected_seeds
    assert len(computed_maps) == len(expected_maps)
    assert computed_maps == expected_maps


def test_find_location_for_initial_seed_unmapped() -> None:
    # Inputs
    in_seed = 14
    maps = {
        "seed-to-soil": [
            (range(98, 100), range(50, 52)),
            (range(50, 98), range(52, 100)),
        ],
        "soil-to-fertilizer": [
            (range(15, 52), range(0, 37)),
            (range(52, 54), range(37, 39)),
            (range(0, 15), range(39, 54)),
        ],
        "fertilizer-to-water": [
            (range(53, 61), range(49, 57)),
            (range(11, 53), range(0, 42)),
            (range(0, 7), range(42, 49)),
            (range(7, 11), range(57, 61)),
        ],
        "water-to-light": [
            (range(18, 25), range(88, 95)),
            (range(25, 95), range(18, 88)),
        ],
        "light-to-temperature": [
            (range(77, 100), range(45, 68)),
            (range(45, 64), range(81, 100)),
            (range(64, 77), range(68, 81)),
        ],
        "temperature-to-humidity": [
            (range(69, 70), range(0, 1)),
            (range(0, 69), range(1, 70)),
        ],
        "humidity-to-location": [
            (range(56, 93), range(60, 97)),
            (range(93, 97), range(56, 60)),
        ],
    }

    # Expected outputs
    expected_location = 43

    # Element Under Test (EUT)
    computed_location = find_location_for_initial_seed(in_seed, maps)

    # Checks
    assert computed_location == expected_location


def test_find_location_for_initial_seed_mapped() -> None:
    # Inputs
    in_seed = 55
    maps = {
        "seed-to-soil": [
            (range(98, 100), range(50, 52)),
            (range(50, 98), range(52, 100)),
        ],
        "soil-to-fertilizer": [
            (range(15, 52), range(0, 37)),
            (range(52, 54), range(37, 39)),
            (range(0, 15), range(39, 54)),
        ],
        "fertilizer-to-water": [
            (range(53, 61), range(49, 57)),
            (range(11, 53), range(0, 42)),
            (range(0, 7), range(42, 49)),
            (range(7, 11), range(57, 61)),
        ],
        "water-to-light": [
            (range(18, 25), range(88, 95)),
            (range(25, 95), range(18, 88)),
        ],
        "light-to-temperature": [
            (range(77, 100), range(45, 68)),
            (range(45, 64), range(81, 100)),
            (range(64, 77), range(68, 81)),
        ],
        "temperature-to-humidity": [
            (range(69, 70), range(0, 1)),
            (range(0, 69), range(1, 70)),
        ],
        "humidity-to-location": [
            (range(56, 93), range(60, 97)),
            (range(93, 97), range(56, 60)),
        ],
    }
    # Expected outputs
    expected_location = 86

    # Element Under Test (EUT)
    computed_location = find_location_for_initial_seed(in_seed, maps)

    # Checks
    assert computed_location == expected_location


def test_solve_part_1() -> None:
    # Inputs
    input_lines = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]

    # Expected outputs
    expected_location = 35

    # Element Under Test (EUT)
    computed_location = solve_part_1(input_lines)

    # Checks
    assert computed_location == expected_location


def test_expand_seeds_list() -> None:
    # Inputs
    base_list = [79, 14, 55, 13]

    # Expected outputs
    expected_ranges_list = [range(79, 93), range(55, 68)]

    # Element Under Test (EUT)
    computed_ranges_list = expand_seeds_list(base_list)

    # Checks
    assert len(computed_ranges_list) == len(expected_ranges_list)
    assert computed_ranges_list == expected_ranges_list


def test_solve_part_2() -> None:
    # Inputs
    input_lines = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]

    # Expected outputs
    expected_location = 46

    # Element Under Test (EUT)
    computed_location = solve_part_2(input_lines)

    # Checks
    assert computed_location == expected_location
