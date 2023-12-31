"""
app.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 29/11/23 11:10:42.524000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from pathlib import Path

from loguru import logger as LOG
from rich import print as pprint
from typer import Argument, Option, Typer
from typing_extensions import Annotated

from aoc2023.common.file_load import load_input_file
from aoc2023.problems.day_1 import compute_calibration_numbers
from aoc2023.problems.day_2 import (
    check_posible_games,
    compute_min_values_per_game,
    compute_sum_of_powers,
)
from aoc2023.problems.day_3 import (
    compute_gear_ratios,
    compute_parts_sum,
    find_gears,
    find_part_numbers,
    parse_lines,
)
from aoc2023.problems.day_4 import solve_part_1 as d4_solve_part_1
from aoc2023.problems.day_4 import solve_part_2 as d4_solve_part_2
from aoc2023.problems.day_5 import solve_part_1 as d5_solve_part_1
from aoc2023.problems.day_5 import solve_part_2 as d5_solve_part_2
from aoc2023.utils.logging_utils import CustomizedLogger, LogConfig, LogLevel
from aoc2023.utils.timing_utils import gen_utc_aware_datetime

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

app = Typer(
    name="aoc2023",
    no_args_is_help=True,
    add_completion=False,
    context_settings=CONTEXT_SETTINGS,
)


@app.callback()
def callback(
    log_level: Annotated[
        LogLevel, Option(..., "--level", "-l", help="Logging level (to file)")
    ] = "OFF"  # type: ignore
) -> None:
    """Callback that executes before every sub-command and can be used to configure logging level.

    Args:
        log_level (str, optional): _description_. Defaults to "OFF".
    """

    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    pprint("+ [bold green]Welcome to Advent of Code 2023 @ferreteleco [white]+")
    print("+++++++++++++++++++++++++++++++++++++++++++++++\n")

    conf = LogConfig()
    now_time = gen_utc_aware_datetime("Europe/Madrid")
    conf.log_conf_path = "logs/" + now_time.strftime("%Y%m%d_%H%M%S_UTC.log")
    conf.log_conf_level_stdout = "OFF"
    conf.log_conf_level_file = log_level.value
    CustomizedLogger.init_logger(conf)


@app.command()
def hello(name: Annotated[str, Argument(..., case_sensitive=True)]) -> None:
    """Basic command greeting.

    Args:
        name (str): Who to greet.
    """

    pprint("[blue]0. Basic greeting command\n")
    LOG.debug(f"Greeting {name}")
    print(f"Hello {name}")


@app.command()
def day1(
    file: Annotated[
        Path,
        Argument(
            ...,
            file_okay=True,
            dir_okay=False,
            resolve_path=True,
            exists=True,
            help="Input data file for the problem",
        ),
    ],
    part: Annotated[
        int,
        Option(
            "--part",
            "-p",
            min=1,
            max=2,
            help="Select the problem part you want to solve",
        ),
    ] = 1,
) -> None:
    """Day one problems interface."""

    pprint("[blue]- Day 1 activity command\n")
    LOG.info("Beginning Day 1 activity!")
    print(f"\tDay 1 input file is in: {file}")

    lines_to_process = load_input_file(file)

    checksum = -1
    match part:
        case 1:
            __, checksum = compute_calibration_numbers(lines_to_process, "digits")
        case 2:
            __, checksum = compute_calibration_numbers(lines_to_process, "alpha")

    pprint(f"\t[bold green]Calibration checksum is {checksum}\n")


@app.command()
def day2(
    file: Annotated[
        Path,
        Argument(
            ...,
            file_okay=True,
            dir_okay=False,
            resolve_path=True,
            exists=True,
            help="Input data file for the problem",
        ),
    ],
    max_values: Annotated[
        tuple[int, int, int],
        Option(
            "--max-values", help="Number of cubes of each type in the bag for the game"
        ),
    ] = (12, 13, 14),
    part: Annotated[
        int,
        Option(
            "--part",
            "-p",
            min=1,
            max=2,
            help="Select the problem part you want to solve",
        ),
    ] = 1,
) -> None:
    """Day two problems interface."""

    pprint("[blue]- Day 2 activity command\n")
    LOG.info("Beginning Day 1 activity!")
    print(f"\tDay 2 input file is in: {file}")

    lines_to_process = load_input_file(file)

    match part:
        case 1:
            __, checksum = check_posible_games(lines_to_process, max_values)
            pprint(f"\t[bold green]Posible games checksum is {checksum}\n")

        case 2:
            min_values_per_game = compute_min_values_per_game(lines_to_process)
            checksum = compute_sum_of_powers(min_values_per_game)
            pprint(f"\t[bold green]Min posible values checksum is {checksum}\n")


@app.command()
def day3(
    file: Annotated[
        Path,
        Argument(
            ...,
            file_okay=True,
            dir_okay=False,
            resolve_path=True,
            exists=True,
            help="Input data file for the problem",
        ),
    ],
    part: Annotated[
        int,
        Option(
            "--part",
            "-p",
            min=1,
            max=2,
            help="Select the problem part you want to solve",
        ),
    ] = 1,
) -> None:
    """Day three problems interface."""

    pprint("[blue]- Day 3 activity command\n")
    LOG.info("Beginning Day 3 activity!")
    print(f"\tDay 3 input file is in: {file}")

    lines_to_process = load_input_file(file)

    match part:
        case 1:
            part_numbers = find_part_numbers(lines_to_process)
            checksum = compute_parts_sum(part_numbers)
            pprint(f"\t[bold green]Part numbers checksum is {checksum}\n")
        case 2:
            parts, symbols = parse_lines(lines_to_process)
            gears = find_gears(parts, symbols)
            computed_gear_ratios = compute_gear_ratios(gears)
            checksum = sum(computed_gear_ratios)
            pprint(f"\t[bold green]Gear ratios checksum is {checksum}\n")


@app.command()
def day4(
    file: Annotated[
        Path,
        Argument(
            ...,
            file_okay=True,
            dir_okay=False,
            resolve_path=True,
            exists=True,
            help="Input data file for the problem",
        ),
    ],
    part: Annotated[
        int,
        Option(
            "--part",
            "-p",
            min=1,
            max=2,
            help="Select the problem part you want to solve",
        ),
    ] = 1,
) -> None:
    """Day four problems interface."""

    pprint("[blue]- Day 4 activity command\n")
    LOG.info("Beginning Day 4 activity!")
    print(f"\tDay 4 input file is in: {file}")

    lines_to_process = load_input_file(file)

    match part:
        case 1:
            points = d4_solve_part_1(lines_to_process)
            pprint(f"\t[bold green]Total points are {points}\n")
        case 2:
            no_cards = d4_solve_part_2(lines_to_process)
            pprint(f"\t[bold green]Final number of cards is {no_cards}\n")


@app.command()
def day5(
    file: Annotated[
        Path,
        Argument(
            ...,
            file_okay=True,
            dir_okay=False,
            resolve_path=True,
            exists=True,
            help="Input data file for the problem",
        ),
    ],
    part: Annotated[
        int,
        Option(
            "--part",
            "-p",
            min=1,
            max=2,
            help="Select the problem part you want to solve",
        ),
    ] = 1,
) -> None:
    """Day five problems interface."""

    pprint("[blue]- Day 5 activity command\n")
    LOG.info("Beginning Day 5 activity!")
    print(f"\tDay 5 input file is in: {file}")

    lines_to_process = load_input_file(file)
    loc = -1
    match part:
        case 1:
            loc = d5_solve_part_1(lines_to_process)
            pprint(f"\t[bold green]Lowest location for initial seeds is {loc}\n")
        case 2:
            loc = d5_solve_part_2(lines_to_process)
    pprint(f"\t[bold green]Lowest location for initial seeds is {loc}\n")
