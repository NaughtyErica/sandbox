# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        pass

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            result = Storm()
        elif isinstance(other, Fire):
            result = Vapor()
        elif isinstance(other, Ground):
            result = Dirt()
        else:
            result = "Не могу смешать {0} и {1}".format(self.__str__(), other.__str__())
        return result


class Air:

    def __init__(self):
        pass

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            result = Storm()
        elif isinstance(other, Fire):
            result = Lightning()
        elif isinstance(other, Ground):
            result = Dust()
        else:
            result = "Не могу смешать {0} и {1}".format(self.__str__(), other.__str__())
        return result


class Fire:

    def __init__(self):
        pass

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            result = Vapor()
        elif isinstance(other, Ground):
            result = Lava()
        elif isinstance(other, Air):
            result = Lightning()
        else:
            result = "Не могу смешать {0} и {1}".format(self.__str__(), other.__str__())
        return result


class Ground:

    def __init__(self):
        pass

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            result = Dirt()
        elif isinstance(other, Air):
            result = Dust()
        elif isinstance(other, Fire):
            result = Lava()
        else:
            result = "Не могу смешать {0} и {1}".format(self.__str__(), other.__str__())
        return result


class Storm:

    def __init__(self):
        pass

    def __str__(self):
        return 'Шторм'


class Vapor:

    def __init__(self):
        pass

    def __str__(self):
        return 'Пар'


class Dirt:

    def __init__(self):
        pass

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __init__(self):
        pass

    def __str__(self):
        return 'Молния'


class Dust:

    def __init__(self):
        pass

    def __str__(self):
        return 'Пыль'


class Lava:

    def __init__(self):
        pass

    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Ground(), '=', Water() + Ground())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Ground(), '=', Air() + Ground())
print(Fire(), '+', Ground(), '=', Fire() + Ground())
print(Ground(), '+', Vapor(), '=', Ground() + Vapor())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
