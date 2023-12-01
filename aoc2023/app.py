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
from aoc2023.day1.problems import compute_calibration_numbers
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
    """Day one problem interface."""

    pprint("[blue]1. Day 1 activity command\n")
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
