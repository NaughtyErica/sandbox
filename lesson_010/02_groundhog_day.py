# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

import random

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day(num_day=0):
    dice = random.randint(1, 13)
    param_carma = 8 - dice
    carma_on_day = abs(param_carma) if param_carma != 0 else 1
    try:
        if dice == 13:
            raise SuicideError('самоубился!')
        elif dice == 12:
            raise DepressionError('впал в дикую депрессию!')
        elif dice == 11:
            raise GluttonyError('обожрался, как свинья!')
        elif dice == 10:
            raise CarCrashError('устроил автокатастрофу!')
        elif dice == 9:
            raise DrunkError('напился до невменяемости!')
        elif dice == 8:
            raise IamGodError('решил, что он Бог!')
    except Exception as exc:
        log_str = f'День {num_day}. Карма {carma_on_day}. Филл {exc} \n'
    else:
        log_str = f'День {num_day}. Карма {carma_on_day}. У Филла был удачный день!\n'
    return carma_on_day, log_str


carma = 0
num_day_cycle = 0
output_file = open('log_fill_days.txt', mode='w', encoding='utf8')

while carma < ENLIGHTENMENT_CARMA_LEVEL:
    num_day_cycle += 1
    result_day = one_day(num_day=num_day_cycle)
    carma += result_day[0]
    output_file.writelines(result_day[1])
output_file.close()

