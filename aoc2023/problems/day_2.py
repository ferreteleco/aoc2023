"""
day_2.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 01/12/23 15:58:04.291000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from loguru import logger as LOG


def compute_min_values_per_game(list_of_games: list[str]) -> list[tuple[int, int, int]]:
    """This function computes the minimum values of each element needed for the game to be posible
    for a list of games encoded as strings (more info on the format in the 'split_game' function).

    Args:
        list_of_games (list[str]): List of game realizations, encoded as strings.

    Returns:
        list[tuple[int, int, int]]: List of minimum elements of each type for a game to be posible,
        for every input game.
    """

    minimum_values_per_game = []
    for game in list_of_games:
        game_id, game_sets = split_game(game)
        min_values = get_min_posible_values_for_game(game_sets)
        LOG.trace("Minimum values for game {} feasibility: {}", game_id, min_values)
        minimum_values_per_game.append(min_values)

    return minimum_values_per_game


def check_posible_games(
    list_of_games: list[str], max_values: tuple[int, int, int]
) -> tuple[list[int], int]:
    """This functions takes a list of games encoded as strings (more info on the format in the
    'split_game' function) and checks if they are posible according to defined max values or not.

    Args:
        list_of_games (list[str]): List of game realizations, encoded as strings.
        max_values (tuple[int, int, int]): List of max values of each cube type, as tuple(reds,
        greens, blues).

    Returns:
        tuple[list[int], int]: List of posible games and sum of their IDs.
    """

    posible_games = []
    for game in list_of_games:
        game_id, game_sets = split_game(game)
        game_posible = is_game_posible(game_sets, max_values)
        LOG.trace("Is game {} posible? -> {}", game_id, game_posible)
        if game_posible:
            posible_games.append(game_id)

    return posible_games, sum(posible_games)


def split_game(game: str) -> tuple[int, list[tuple[int, int, int]]]:
    """Splits a game defined as a string with the format:

    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'

    Into a game id and a list of tuples of game sets. Note that each set is delimited by ';' and the
    order and number of colors in each set is variable and unordered.

    Args:
        game (str): Game definition string.

    Returns:
        tuple[int, list[tuple[int, int, int]]]: Game ID and list of game sets as integers (n_red,
        n_green, n_blue)
    """

    game_tokens = game.split(":")
    game_id = int(game_tokens[0].strip()[5:])

    LOG.trace("Splitting game string {} sets into format", game_id)

    sets = game_tokens[1].strip().split(";")

    game_sets = []
    for set_i in sets:
        items = set_i.strip().split(",")

        red_n = 0
        blue_n = 0
        green_n = 0
        for item in items:
            parts = item.strip().split(" ")
            n_balls = int(parts[0].strip())
            match parts[1].strip():
                case "red":
                    red_n = n_balls
                case "green":
                    green_n = n_balls
                case "blue":
                    blue_n = n_balls
        game_sets.append((red_n, green_n, blue_n))

    return game_id, game_sets


def is_game_posible(
    game_sets: list[tuple[int, int, int]], max_values: tuple[int, int, int]
) -> bool:
    """Checks whether a given game (defined by a list of tuples of realizations) is posible or not.

    This condition is set by an additional tuple that indicates how many cubes of each type are in
    the bag for a game.

    Args:
        game_sets (list[tuple[int, int, int]]): List of sets of a particular game.
        max_values (tuple[int, int, int]): Number of cubes of each type (red, green, blue) stored
        in the bag for the game.

    Returns:
        bool: Whether the game is posible or not.
    """

    LOG.trace("Checking game feasibility")
    posible = not any(
        any([x > y for (x, y) in zip(game_set, max_values)]) for game_set in game_sets
    )

    return posible


def get_min_posible_values_for_game(
    game_sets: list[tuple[int, int, int]]
) -> tuple[int, int, int]:
    """Computes the minimum values of each element needed for the game to be posible.

    Args:
        game_sets (list[tuple[int, int, int]]): List of sets of a particular game.

    Returns:
        tuple[int, int, int]: Minimum number of elements of each type required for the game to be
        valid, defined as (red, green, blue) tuple.
    """

    LOG.trace("Computing minimum values for game")

    min_red = max(game_sets, key=lambda x: x[0])[0]
    min_green = max(game_sets, key=lambda x: x[1])[1]
    min_blue = max(game_sets, key=lambda x: x[2])[2]

    return (min_red, min_green, min_blue)


def compute_sum_of_powers(values_per_game: list[tuple[int, int, int]]) -> int:
    """Computes the sum of the powers of a group of game realizations. The power of a realization
    is equal to the numbers of red, green, and blue multiplied together.

    Args:
        values_per_game (list[tuple[int, int, int]]): Elements of each type in a game realization.

    Returns:
        int: Sum of the products of the different types of cubes in a game.
    """

    LOG.trace("Computing sum of powers for group of game realizations")
    sum_of_powers = sum([mv[0] * mv[1] * mv[2] for mv in values_per_game])

    return sum_of_powers
