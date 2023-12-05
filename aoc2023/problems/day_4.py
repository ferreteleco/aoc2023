"""
day_4.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 05/12/23 01:52:53.391000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from loguru import logger as LOG
from regex import findall, split


def parse_input(raw_lines: list[str]) -> list[tuple[list[int], list[int]]]:
    """Parses a given list of game strings that contain a card ID ended by ':', a list of wining
    numbers and a list of card numbers, both separated by the '|' character. This function returns a
    list of tuples (that represent the winning numbers and the card numbers respectively).

    Args:
        raw_lines (list[str]): List of raw input lines.

    Returns:
        list[tuple[list[int], list[int]]]: Processed cards and winning numbers.
    """

    LOG.trace(
        "Parsing {} input raw cards into winning and card numbers", len(raw_lines)
    )
    pattern_find = r"\d+"
    pattern_split = r"[:\|]"

    games = []
    for line in raw_lines:
        parts = split(pattern_split, line)
        winning_numbers = [int(num) for num in findall(pattern_find, parts[1])]
        card_numbers = [int(num) for num in findall(pattern_find, parts[2])]

        games.append((winning_numbers, card_numbers))

    return games


def check_card_points(card: tuple[list[int], list[int]]) -> tuple[list[int], int]:
    """Check the number of points obtained for a given card. The points are awarded by checking which
    of the numbers you have appear in the list of winning numbers. The first match makes the card
    worth one point and each match after the first doubles the point value of that card.

    Args:
        card (tuple[list[int], list[int]]): Winning numbers and card numbers for a given card.

    Returns:
        tuple[list[int], int]: List of winning number present in the card's number and value of the
        card in points.
    """

    LOG.trace("Checking card's worth in points")

    hits = [number for number in card[1] if number in card[0]]
    points = 2 ** (len(hits) - 1) if hits else 0

    LOG.trace(
        "Card has {} winning numbers ({})! It's worth {} points",
        len(hits),
        hits,
        points,
    )

    return hits, points


def solve_part_1(raw_lines: list[str]) -> int:
    """Solves the first problem.

    Args:
        raw_lines (list[str]): List of raw input lines.

    Returns:
        int: Total points for the set of cards.
    """

    list_of_cards = parse_input(raw_lines)
    total_points = [check_card_points(card)[1] for card in list_of_cards]

    return sum(total_points)


def accumulate_cards(
    list_of_cards: list[tuple[list[int], list[int]]]
) -> dict[int, int]:
    """Scratchcards only cause you to win more scratchcards equal to the number of winning numbers
    you have.

    Specifically, you win copies of the scratchcards below the winning card equal to the number of
    matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11,
    12, 13, 14, and 15.

    Copies of scratchcards are scored like normal scratchcards and have the same card number as the
    card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then
    win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This
    process repeats until none of the copies cause you to win any more cards. (Cards will never make
    you copy a card past the end of the table.)

    Args:
        list_of_cards (list[tuple[list[int], list[int]]]): Input list of cards.

    Returns:
        dict[int, int]: Dictionary indicating how many copies of each card you have after processing
        the original list.
    """

    extended_card_ids = {index + 1: 1 for index in range(len(list_of_cards))}
    for index, card in enumerate(list_of_cards):
        hits, __ = check_card_points(card)
        aff_ids = range(index + 2, index + len(hits) + 2)

        for aff_id in aff_ids:
            extended_card_ids[aff_id] += 1 * extended_card_ids[index + 1]

    return extended_card_ids


def solve_part_2(raw_lines: list[str]) -> int:
    """Solves the second problem.

    Args:
        raw_lines (list[str]): List of raw input lines.

    Returns:
        int: Total number of scratchcards after processing.
    """

    list_of_cards = parse_input(raw_lines)
    extended_card_ids = accumulate_cards(list_of_cards)

    return sum(extended_card_ids.values())
