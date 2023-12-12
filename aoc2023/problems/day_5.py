"""
day_5.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 07/12/23 13:46:05.868000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from regex import findall


def initialize_dicts() -> dict[str, list[tuple[range, range]]]:
    dicts = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    return dicts


def parse_lines(
    raw_rows: list[str],
) -> tuple[list[int], dict[str, list[tuple[range, range]]]]:
    num_pattern = r"\d+"
    text_pattern = r"\D+(?= )"

    seed_ids = [int(seed) for seed in findall(num_pattern, raw_rows[0])]
    dicts = initialize_dicts()
    dict_name = ""
    flag = False
    for row in raw_rows[1:]:
        if row == "":
            flag = True
        elif flag:
            dict_name = findall(text_pattern, row)[0]
            flag = False
        else:
            tokens = findall(num_pattern, row)
            dicts[dict_name].append(
                (
                    range(int(tokens[1]), int(tokens[1]) + int(tokens[2])),
                    range(int(tokens[0]), int(tokens[0]) + int(tokens[2])),
                )
            )

    return seed_ids, dicts


def find_location_for_initial_seed(
    seed: int, maps: dict[str, list[tuple[range, range]]]
) -> int:
    var = seed
    for __, mp in maps.items():
        for src, dst in mp:
            if var in src:
                var = dst[var - src[0]]
                break

    return var


def solve_part_1(raw_lines: list[str]) -> int:
    seeds, maps = parse_lines(raw_lines)
    locations = [find_location_for_initial_seed(seed, maps) for seed in seeds]

    return min(locations)


def expand_seeds_list(input_list: list[int]) -> list[range]:
    expanded_list = []
    for start, n in zip(input_list[0::2], input_list[1::2]):
        expanded_list.append(range(start, start + n))

    return expanded_list


def solve_part_2(raw_lines: list[str]) -> int:
    seeds_base, maps = parse_lines(raw_lines)
    seed_ranges = expand_seeds_list(seeds_base)

    locations = []
    for seed_range in seed_ranges:
        locations.extend(
            [find_location_for_initial_seed(seed, maps) for seed in seed_range]
        )

    return min(locations)
