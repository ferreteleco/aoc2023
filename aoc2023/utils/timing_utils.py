"""
timing_utils.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 29/11/23 13:59:11.210000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from __future__ import annotations

from datetime import datetime
from time import perf_counter

from loguru import logger as LOG
from pytz import timezone, utc
from rich import print as pprint


def gen_utc_aware_datetime(tz_name: str, timestamp: (float | None) = None) -> datetime:
    """Generates a UTC timestamp with awareness of the current time zone.

    Ref.: https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
    aka from pytz import all_timezones

    Ref.: https://stackoverflow.com/questions/1357711/pytz-utc-conversion

    Args:
        tz_name (str): Local timezone name.
        timestamp (float | None, optional): Timestamp to be used, if specified. Else, "now".
    Returns:
        datetime: Datetime (UTC)
    """

    tz = timezone(tz_name)
    return (
        tz.normalize(tz.localize(datetime.fromtimestamp(timestamp))).astimezone(utc)
        if timestamp
        else tz.normalize(tz.localize(datetime.now())).astimezone(utc)
    )


def perf_timer(decorator_name: str | None = None):
    """Decorator to time a function.

    Args:
        decorator_name (str | None, optional): Optional decorator name. Defaults to None (function
        name).
    """

    def decorator(func):
        def wrapper(*args, **kwargs):

            if decorator_name:
                name = decorator_name
            else:
                name = func.__name__

            try:
                start = perf_counter()
                result = func(*args, **kwargs)
                delta = (perf_counter() - start) * 1000

                msg = f"Finished {name} in {delta:.4f} ms"
                pprint(f"[bold yellow]{msg}\n")
                LOG.debug(msg)

            except Exception as e:  # pylint: disable=broad-exception-caught
                LOG.exception("Exception when solving {}: {}", name, e)
            else:
                return result

        return wrapper

    return decorator
