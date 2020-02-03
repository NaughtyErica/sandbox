import logging.config
from lesson_014.python_snippets.primes_package.primes import prime_numbers_generator
from lesson_014.python_snippets.primes_package.log_settings import log_config

# import logging
# main_log = logging.getLogger('main')
# main_log.setLevel(logging.DEBUG)
# main_fh = logging.FileHandler("main.log", 'w', 'utf-8')
# main_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# main_fh.setFormatter(main_formatter)
# main_log.addHandler(main_fh)


logging.config.dictConfig(log_config)
main_log = logging.getLogger('main')


def print_primes(n):
    for prime in prime_numbers_generator(n):
        main_log.info(f'Простое из генераторв {prime}')


if __name__ == '__main__':
    print_primes(n=10)
