"""
test_day_2.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 02/12/23 22:07:15.556000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""


from aoc2023.problems.day_2 import (
    check_posible_games,
    compute_min_values_per_game,
    compute_sum_of_powers,
    get_min_posible_values_for_game,
    is_game_posible,
    split_game,
)


def test_split_game() -> None:
    """Tests the function that splits a game iteration into id and sets."""

    # Inputs
    game = "Game 3: 8 green, 6 blue, 20 red; 2 blue, 4 red, 13 green; 5 green, 1 red"

    # Expected outputs
    expected_game_id = 3
    expected_game_sets = [(20, 8, 6), (4, 13, 2), (1, 5, 0)]

    # Element Under Test (EUT)
    computed_id, computed_sets = split_game(game)

    # Checks
    assert computed_id == expected_game_id
    assert len(computed_sets) == len(expected_game_sets)
    assert computed_sets == expected_game_sets


def test_is_game_posible_true() -> None:
    """Test the function that checks if a game is posible or not for the case where it posible."""

    # Inputs
    game_sets = [(5, 8, 6), (4, 13, 5), (1, 5, 0)]

    max_values = (12, 13, 14)

    # Expected outputs
    expected_posible = True

    # Element Under Test (EUT)
    computed_posible = is_game_posible(game_sets, max_values)

    # Checks
    assert computed_posible == expected_posible


def test_is_game_posible_too_many_reds() -> None:
    """Test the function that checks if a game is posible or not for the case where it is not
    posible due to more red values than defined.
    """

    # Inputs
    game_sets = [(20, 8, 6), (4, 13, 5), (1, 5, 0)]

    max_values = (12, 13, 14)

    # Expected outputs
    expected_posible = False

    # Element Under Test (EUT)
    computed_posible = is_game_posible(game_sets, max_values)

    # Checks
    assert computed_posible == expected_posible


def test_is_game_posible_too_many_greens() -> None:
    """Test the function that checks if a game is posible or not for the case where it is not
    posible due to more green values than defined.
    """

    # Inputs
    game_sets = [(0, 8, 6), (4, 13, 5), (1, 15, 0)]

    max_values = (12, 13, 14)

    # Expected outputs
    expected_posible = False

    # Element Under Test (EUT)
    computed_posible = is_game_posible(game_sets, max_values)

    # Checks
    assert computed_posible == expected_posible


def test_is_game_posible_too_many_blues() -> None:
    """Test the function that checks if a game is posible or not for the case where it is not
    posible due to more blue values than defined.
    """

    # Inputs
    game_sets = [(0, 8, 6), (4, 13, 5), (1, 5, 40)]

    max_values = (12, 13, 14)

    # Expected outputs
    expected_posible = False

    # Element Under Test (EUT)
    computed_posible = is_game_posible(game_sets, max_values)

    # Checks
    assert computed_posible == expected_posible


def test_day_2_possible_games() -> None:
    """Test the logic that checks the feasibility of a list of games."""

    # Inputs
    list_of_games = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    max_values = (12, 13, 14)

    # Expected outputs
    expected_posible_games_ids = [1, 2, 5]
    expected_sum_posible_games_ids = 8

    # Element Under Test (EUT)
    computed_posible_games, computed_posible_ids_sum = check_posible_games(
        list_of_games, max_values
    )

    # Checks
    assert len(computed_posible_games) == len(expected_posible_games_ids)
    assert computed_posible_games == expected_posible_games_ids
    assert computed_posible_ids_sum == expected_sum_posible_games_ids


def test_day_2_minimum_number_of_cubes_per_game():

    # Inputs
    list_of_games = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    # Expected outputs
    expected_min_values_per_game = [
        (4, 2, 6),
        (1, 3, 4),
        (20, 13, 6),
        (14, 3, 15),
        (6, 3, 2),
    ]

    # Element Under Test (EUT)
    computed_min_values_per_game = compute_min_values_per_game(list_of_games)

    # Checks
    assert len(computed_min_values_per_game) == len(expected_min_values_per_game)
    assert computed_min_values_per_game == expected_min_values_per_game


def test_get_min_posible_values_for_game() -> None:
    """Tests the function that computes the minimum required number of elements of each type for a
    game to be posible.
    """

    # Inputs
    game_sets = [(0, 8, 6), (4, 13, 5), (1, 5, 40)]

    # Expected outputs
    expected_min_values = (4, 13, 40)

    # Element Under Test (EUT)
    computed_min_values = get_min_posible_values_for_game(game_sets)

    # Checks
    assert computed_min_values == expected_min_values


def test_compute_sum_of_powers() -> None:
    """Test the function that computes the sum of powers of a group of game sets."""

    # Inputs
    values_per_game = [
        (4, 2, 6),
        (1, 3, 4),
        (20, 13, 6),
        (14, 3, 15),
        (6, 3, 2),
    ]

    # Expected outputs
    expected_sum = 2286

    # Element Under Test (EUT)
    computed_sum = compute_sum_of_powers(values_per_game)

    # Checks
    assert computed_sum == expected_sum
