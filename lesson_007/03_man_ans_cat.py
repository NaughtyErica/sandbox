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

# TODO Изменил начальные условия для большей правдоподобности: Челокеп подбирает сытых животных,
# TODO но приходит в пустой дом. Изменил логику подыхания от голода - животное умирает в конце дня
# TODO и уже не участвует в дальнейшей "жизни". Собака инициирует драку, но только с сытым котом

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class House:
    def __init__(self):
        self.food = 0
        self.animal_food = 0
        self.money = 0
        self.debris = 0
        self.number_fighting_cat = 0

    def __str__(self):
        return 'В доме еды для людей осталось {}, еды для животных -- {}, денег -- {}, грязи -- {}'.format(
            self.food, self.animal_food, self.money, self.debris)


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.living = True

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
            cprint('{} сходил в магазин за своей едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} не хватает денег на покупку своей еды!'.format(self.name), color='red')

    def shopping_animal_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для животных'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.animal_food += 50
        else:
            cprint('{} не хватает денег на покупку еды для животных!'.format(self.name), color='red')

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

    def pick_up_dog(self, dog):
        dog.house = self.house
        cprint('Собаку {} подобрал {} и принес в дом'.format(dog.name, self.name), color='cyan')

    def act(self):
        if self.living:
            dice = randint(1, 6)
            if self.fullness < 0:
                cprint('{} умер...'.format(self.name), color='red')
                self.living = False
                return
            if self.fullness < 20:
                self.eat()
            elif self.house.money <= 50:
                self.work()
            elif self.house.food <= 10:
                self.shopping()
            elif self.house.animal_food <= 30:
                self.shopping_animal_food()
            elif self.house.debris >= 100:
                self.clearn_house()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                self.watch_MTV()
        else:
            cprint('==================', color='red')


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.living = True

    def __str__(self):
        if self.living:
            if self.fullness < 0:
                cprint('Кот {} умер...'.format(self.name), color='red')
                self.living = False

            str_print = 'Я кот - {}, сытость {}'.format(self.name, self.fullness)
        else:
            str_print = '========================='
        return str_print

    def eat(self):
        if self.house.animal_food >= 10:
            cprint('Кот {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.animal_food -= 10
        else:
            self.fullness -= 10
            cprint('У кота {} нет еды. Остался голодный на всесь день'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} дрых весь день'.format(self.name), color='blue')

    def strip_wallpaper(self):
        self.fullness -= 10
        self.house.debris += 5
        cprint('Кот {} подрал обои'.format(self.name), color='red')

    def fight_with_dog(self, cat, dog):
        self.fullness -= 10
        self.house.debris += 5
        self.house.number_fighting_cat = 0
        cprint('Кот {} дрался с собакой {}'.format(cat.name, dog.name), color='red')

    def act(self, cat=None):
        if self.living:
            dice = randint(1, 6)
            if self.house.number_fighting_cat == 1 and cat == cat1:
                self.fight_with_dog(cat=cat1, dog=dog1)
            elif self.house.number_fighting_cat == 2 and cat == cat2:
                self.fight_with_dog(cat=cat2, dog=dog1)
            else:
                if self.fullness < 20:
                    self.eat()
                elif dice in (1, 3, 5):
                    self.sleep()
                else:
                    self.strip_wallpaper()
        else:
            cprint('=======================', color='red')


class Dog:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.living = True

    def __str__(self):
        if self.living:
            if self.fullness < 0:
                cprint('Собака {} умерла...'.format(self.name), color='red')
                self.living = False
            str_print = 'Я собака - {}, сытость {}'.format(self.name, self.fullness)
        else:
            str_print = '========================='
        return str_print

    def eat(self):
        if self.house.animal_food >= 10:
            cprint('Собака {} поела'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.animal_food -= 10
        else:
            self.fullness -= 10
            cprint('У собаки {} нет еды, осталась голодная на весь день'.format(self.name), color='red')

    def crew_furniture(self):
        self.fullness -= 10
        self.house.debris += 5
        cprint('Собака {} грызла мебель'.format(self.name), color='red')

    def fight_with_cat(self, cat):
        self.fullness -= 10
        self.house.debris += 5
        cprint('Собака {} дралась с котом {}'.format(self.name, cat.name), color='red')

    def act(self):
        if self.living:
            dice = randint(1, 4)
            self.house.number_fighting_cat = 0
            if self.fullness < 20:
                self.eat()
            elif dice == 1 and cat1.living and cat1.fullness > 10:
                self.house.number_fighting_cat = 1
                self.fight_with_cat(cat=cat1)
            elif dice == 2 and cat2.living and cat2.fullness > 10:
                self.house.number_fighting_cat = 2
                self.fight_with_cat(cat=cat2)
            else:
                self.crew_furniture()
        else:
            cprint('=======================', color='red')


mark = Man(name='Марк')
my_sweet_home = House()
dog1 = Dog(name='Жучка')
cat1 = Cat(name='Мурзик')
cat2 = Cat(name='Барсик')
mark.go_to_the_house(house=my_sweet_home)
mark.pick_up_dog(dog=dog1)
mark.pick_up_cat(cat=cat1)
mark.pick_up_cat(cat=cat2)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    mark.act()
    dog1.act()
    cat1.act(cat=cat1)
    cat2.act(cat=cat2)
    print('--- в конце дня ---')
    print(mark)
    print(dog1)
    print(cat1)
    print(cat2)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.
# (Можно определить критическое количество котов, которое может прокормить человек...)
