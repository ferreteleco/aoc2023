"""
logging_utils.py

Project: Advent of Code 2023

Maintainer Andrés Ferreiro González (andres.ferreiro.glez@gmail.com)
Created @ 29/11/23 13:43:01.662000

Copyright (c) 2023 Andrés Ferreiro González
See project license for more info
"""

from __future__ import annotations

import json
import logging
import sys
from enum import Enum, unique

from loguru import logger as LOG
from pydantic import BaseModel, validator


@unique
class LogLevel(Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    OFF = "OFF"

    @classmethod
    def to_list(cls) -> list[str]:
        """Returns a list with all the elements in the enum.

        Returns:
            List[str]: List all levels of the LogLevel enum.
        """

        return [el.value for el in cls]


class LogConfig(BaseModel):
    """Log configuration container object. For more info, see:

    * https://loguru.readthedocs.io/en/stable/api/logger.html
    """

    log_conf_path: (str | None) = None
    log_conf_level_stdout: str = "INFO"
    log_conf_level_file: str = "DEBUG"
    log_conf_rotation: (str | None) = None
    log_conf_retention: (str | None) = None
    log_conf_compression: (str | None) = None
    log_conf_backtrace: bool = False
    log_conf_enqueue: bool = False
    log_conf_colorize: bool = False
    log_conf_format: str = "{time:YYYY-MM-DD HH:mm:ss.SSS Z} | {level: <8} | {name}:{function}:{line} - {message}"  # noqa: B950

    @validator("log_conf_level_stdout", "log_conf_level_file")
    def sanitize_log_levels(cls, value):  # pylint: disable=no-self-argument
        new_value = value.upper()

        if new_value not in LogLevel.to_list():
            raise ValueError("Log defined log level is not valid!")

        return new_value

    @validator(
        "log_conf_path",
        "log_conf_rotation",
        "log_conf_retention",
        "log_conf_compression",
        pre=True,
        always=True,
    )
    def validate_nones(cls, value):  # pylint: disable=no-self-argument
        if not value:
            return None
        if isinstance(value, str) and value.upper() in {"NONE", "NULL"}:
            return None
        return value

    @validator("log_conf_compression", always=True)
    def validate_compression(cls, value):  # pylint: disable=no-self-argument
        if value and value not in [
            "gz",
            "bz2",
            "xz",
            "lzma",
            "tar",
            "tar.gz",
            "tar.bz2",
            "tar.xz",
            "zip",
        ]:
            raise ValueError(f"Compression value not valid {value}")
        return value


class InterceptHandler(logging.Handler):
    """Intercept handler para redirigir el tráfico de los módulos que emplean el logger estándar de
    python a loguru.
    """

    loglevel_mapping = {
        50: "CRITICAL",
        40: "ERROR",
        30: "WARNING",
        20: "INFO",
        10: "DEBUG",
        5: "TRACE",
        0: "NOTSET",
    }

    def emit(self, record):
        try:
            level = LOG.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # type: ignore (does not fail)
            frame = frame.f_back  # type: ignore (does not fail)
            depth += 1

        LOG.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


class CustomizedLogger:
    """Logger customizado loguru que recibe configuración de la app para generar un log pantalla y
    opcionalmente un log en fichero.
    """

    @classmethod
    def init_logger(cls, config: LogConfig):
        LOG.remove()

        if config.log_conf_level_stdout != "OFF":
            LOG.add(
                sys.stdout,
                enqueue=config.log_conf_enqueue,
                backtrace=config.log_conf_backtrace,
                level=config.log_conf_level_stdout,
                format=config.log_conf_format,
                colorize=config.log_conf_colorize,
            )

        if config.log_conf_path and config.log_conf_level_file != "OFF":
            LOG.add(
                config.log_conf_path,
                rotation=config.log_conf_rotation,
                retention=config.log_conf_retention,
                enqueue=config.log_conf_enqueue,
                backtrace=config.log_conf_backtrace,
                level=config.log_conf_level_file.upper(),
                format=config.log_conf_format,
                compression=config.log_conf_compression,
            )

        logging_level_dict = {
            "CRITICAL": 50,
            "ERROR": 40,
            "WARNING": 30,
            "INFO": 20,
            "DEBUG": 10,
            "TRACE": 10,
            "NOTSET": 0,
        }

        # Impl. Notes (20220222-aferreiro) Unify logging for a Gunicorn/Uvicorn/FastAPI application
        # https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/

        logging.root.handlers = [InterceptHandler()]
        logging.root.setLevel(
            min(
                logging_level_dict.get(config.log_conf_level_stdout.upper(), 0),
                logging_level_dict.get(config.log_conf_level_file.upper(), 0),
            )
        )

        for name in logging.root.manager.loggerDict:  # pylint: disable=no-member
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        return LOG.bind(request_id=None, method=None)

    @classmethod
    def load_logging_conf(cls, config_path):
        config = None
        with open(config_path, encoding="utf-8") as config_file:
            config = json.load(config_file)
        return config
