# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import lesson_005.my_burger as bg


def double_cheeseburger():
    bg.add_ban_start()
    bg.add_cutlet()
    bg.add_cheese()
    bg.add_cutlet()
    bg.add_cheese()
    bg.add_cucumber()
    bg.add_ketchup()
    bg.add_onions()
    bg.add_mustard()
    bg.add_ban_finish()


def my_burger():
    bg.add_ban_start()
    bg.add_salad()
    bg.add_mayonnaise()
    bg.add_cheese()
    bg.add_cutlet()
    bg.add_mayonnaise()
    bg.add_cheese()
    bg.add_salad()
    bg.add_ketchup()
    bg.add_ban_finish()


double_cheeseburger()

my_burger()

# зачет! Неплохо было бы в начале создания бургера выводить пояснение: название бургера, например.
