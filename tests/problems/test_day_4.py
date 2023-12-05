"""
test_day_4.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 05/12/23 02:03:09.115000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""


from aoc2023.problems.day_4 import (
    accumulate_cards,
    check_card_points,
    parse_input,
    solve_part_1,
    solve_part_2,
)


def test_parse_input() -> None:
    """Test the function that parses the games and winning numbers raw strings."""

    # Inputs
    raw_rows = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    ]
    # Expected outputs
    expected_games = [
        ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
        ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
        ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
    ]

    # Element Under Test (EUT)
    computed_games = parse_input(raw_rows)

    # Checks
    assert len(computed_games) == len(expected_games)
    for comp, exp in zip(computed_games, expected_games):
        assert len(comp) == len(exp)
        assert len(comp[0]) == len(exp[0])
        assert len(comp[1]) == len(exp[1])
        assert comp[0] == exp[0]
        assert comp[1] == exp[1]


def test_check_card_points() -> None:
    """Test the function that checks the number of points for a given game."""

    # Inputs
    game = ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])

    # Expected outputs
    expected_hits = [83, 86, 17, 48]
    expected_points = 8

    # Element Under Test (EUT)
    computed_hits, computed_points = check_card_points(game)

    # Checks
    assert computed_points == expected_points
    assert len(computed_hits) == len(expected_hits)
    assert computed_hits == expected_hits


def test_check_card_points_no_hits() -> None:
    """Test the function that checks the number of points for a given game where there are no
    winning numbers in the card."""

    # Inputs
    game = ([41, 58, 23, 6, 77], [83, 86, 26, 31, 17, 9, 48, 53])

    # Expected outputs
    expected_hits = []
    expected_points = 0

    # Element Under Test (EUT)
    computed_hits, computed_points = check_card_points(game)

    # Checks
    assert computed_points == expected_points
    assert len(computed_hits) == len(expected_hits)
    assert computed_hits == expected_hits


def test_solve_part_1() -> None:
    """Checks the resolution of the first problem for the day."""

    # Inputs
    raw_rows = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    ]

    # Expected outputs
    expected_points = 13

    # Element Under Test (EUT)
    computed_points = solve_part_1(raw_rows)

    # Checks
    assert computed_points == expected_points


def test_accumulate_cards() -> None:
    """Tests the function that extends the list of cards according to the instructions."""

    # Inputs
    games = [
        ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
        ([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
        ([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
        ([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
        ([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
        ([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]),
    ]

    # Expected outputs
    expected_extended_ids = {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}

    # Element Under Test (EUT)
    computed_extended_ids = accumulate_cards(games)

    assert computed_extended_ids == expected_extended_ids


def test_solve_part_2() -> None:
    """Checks the resolution of the second problem for the day."""

    # Inputs
    raw_rows = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    # Expected outputs
    expected_cards_no = 30

    # Element Under Test (EUT)
    computed_cards_no = solve_part_2(raw_rows)

    # Checks
    assert computed_cards_no == expected_cards_no
