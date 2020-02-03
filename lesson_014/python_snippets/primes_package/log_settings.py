# -*- coding: utf-8 -*-

log_config = {
    "version": 1,
    "formatters": {
        "primes_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
        "main_formatter": {
            "format": "%(asctime)s - %(message)s",
            "datefmt": "%d-%m-%Y %H:%M:%S",
        },
    },
    "handlers": {
        "primes_handler": {
            "class": "logging.FileHandler",
            "formatter": "primes_formatter",
            "filename": "primes.log",
            "encoding": "UTF-8",
        },
        "main_handler": {
            "class": "logging.FileHandler",
            "formatter": "main_formatter",
            "filename": "main.log",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "primes": {
            "handlers": ["primes_handler"],
            "level": "DEBUG",
        },
        "main": {
            "handlers": ["main_handler"],
            "level": "INFO",
        },
    },
}

