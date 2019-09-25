# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кошачей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clearn_house(self):
        self.house.debris -= 100
        self.fullness -= 20
        cprint('{} убирался в доме'.format(self.name), color='cyan')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def pick_up_cat(self, cat):
        cat.house = self.house
        cprint('Кота {} подобрал {} и принес в дом'.format(cat.name, self.name), color='cyan')


    def act(self):
        dice = randint(1, 6)
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return

        if self.fullness < 20:
            self.eat()
        elif self.house.money < 50:
            self.work()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.cat_food <= 10:
            self.shopping_cat_food()
        elif self.house.debris >= 100:
            self.clearn_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 0
        self.cat_food = 0
        self.money = 0
        self.debris = 0

    def __str__(self):
        return 'В доме еды для людей осталось {}, кошачей еды -- {}, денег -- {}, грязи --{}'.format(
            self.food, self.cat_food, self.money, self.debris)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('У кота {} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} дрых весь день'.format(self.name), color='blue')

    def strip_wallpaper(self):
        self.fullness -= 10
        self.house.debris += 10
        cprint('Кот {} подрал обои'.format(self.name), color='red')

    def act(self):
        dice = randint(1, 6)
        if self.fullness < 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.strip_wallpaper()



mark = Man(name='Марк')
my_sweet_home = House()
cat1 = Cat(name='Мурзик')
cat2 = Cat(name='Барсик')
mark.go_to_the_house(house=my_sweet_home)
mark.pick_up_cat(cat=cat1)
mark.pick_up_cat(cat=cat2)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    mark.act()
    cat1.act()
    cat2.act()
    print('--- в конце дня ---')
    print(mark)
    print(cat1)
    print(cat2)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
