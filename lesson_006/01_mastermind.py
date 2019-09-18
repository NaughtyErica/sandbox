# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

import lesson_006.mastermind_engine as me
user_input_str = ''


def validator_input_number(input_str=''):
    while True:
        if input_str[0] != '0' and input_str.isdigit() and len(set(input_str)) == 4:
            return input_str
        else:
            print('Не корректный ввод! Допустимые значания 1234567890, \n'
                  'четыре цифры, все разные, первая не 0')
            input_str = input('Попробуйте еще раз -->')


def validator_yse_no(input_str=''):
    while input_str not in ('y', 'n'):
        print('Не корректный ввод! Допустимые значания y/n')
        input_str = input('Попробуйте еще раз -->')
    return input_str


print('Начинаем игру "Быки и Коровы". Я задумываю четырехзначное число,\n'
      'все цифры которого различны (первая цифра числа отлична от нуля).\n'
      'Вам необходимо разгадать задуманное число. Вы вводите четырехзначное\n'
      'число c неповторяющимися цифрами, я сообщаю о количестве «быков» и «коров»\n'
      'в названном числе. «Бык» — цифра есть в записи задуманного числа и стоит\n'
      'в той же позиции, что и в задуманном числе, «Корова» — цифра есть в записи\n'
      'задуманного числа, но не стоит в той же позиции, что в задуманном числе')


while True:
    step_game = 0
    me.pick_number()
    print('Я загадал четырехзначное число, попытайтесь его отгадать')
    while True:
        user_input_str = input('Введите число или <q> если сдаетесь --> ')
        if user_input_str == 'q':
            print('Очень жаль, что не закончили партию!')
            raise SystemExit(0)
        else:
            user_input_str = validator_input_number(input_str=user_input_str)
            result = me.check_number(user_input_str=user_input_str)
            print('Быки -', result['bulls'], 'Коровы -', result['cows'])
            step_game += 1
            if result['bulls'] == 4:
                print('Вы угадали за', step_game, 'ходов')
                continue_or_exit = validator_yse_no(input_str=input('Хотите еще партию? <y/n>'))
                if continue_or_exit == 'n':
                    print('Спасибо за игру!')
                    raise SystemExit(0)
                else:
                    break
