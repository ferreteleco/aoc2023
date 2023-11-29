"""
app.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 29/11/23 11:10:42.524000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from typer import Typer

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}

app = Typer(
    name="aoc2023",
    no_args_is_help=True,
    add_completion=True,
    context_settings=CONTEXT_SETTINGS,
)


@app.command()
def hello(name: str) -> None:
    """Basic command greeting.

    Args:
        name (str): Who to greet.
    """

    print(f"Hello {name}")


@app.command()
def day1(filename: str) -> None:
    """Day one problem interface.

    Args:
        filename (str): File to be loaded.
    """

    print(f"Day 1: {filename}")
