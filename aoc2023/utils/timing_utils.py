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

from pytz import timezone, utc


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
