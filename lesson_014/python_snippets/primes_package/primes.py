# -*- coding: utf-8 -*-

import logging.config
from lesson_014.python_snippets.primes_package.log_settings import log_config


# log = logging.getLogger('primes')
# log.setLevel(logging.DEBUG)
# fh = logging.FileHandler("primes.log", 'w', 'utf-8')
# formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# datefmt="%d-%m-%Y- %H:%M:%S")
# fh.setFormatter(formatter)
# log.addHandler(fh)


logging.config.dictConfig(log_config)
primes_log = logging.getLogger('primes')


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        primes_log.debug(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                primes_log.debug(f'делится на {prime}')
                break
        else:
            primes_log.debug(f'найдено новое простое {number}')
            prime_numbers.append(number)
            yield number


