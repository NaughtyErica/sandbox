# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42
input_data = ''
try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    lee_loo = int(input_data[4])
except ValueError:
    print(f'{input_data[4]} не является числом!')
except IndexError:
    print('Нет пятого элеменнта в веденном списке!')
except:
    print('Ошибка ввода!')
else:
    result = BRUCE_WILLIS * lee_loo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения EOFError
# для каждого типа исключений написать на консоль соотв. сообщение




