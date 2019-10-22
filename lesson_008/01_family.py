# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.total_food = 50
        self.animal_food = 30
        self.money = 100
        self.debris = 0
        self.list_cats = []
        self.quantity_cats = 0

    def __str__(self):
        return 'В доме еды для людей {}, еды для котов {}, денег  {}, грязи  {}'.format(
            self.food, self.animal_food, self.money, self.debris)

    def act(self):
        self.debris += 5

    def get_food(self):
        return self.food

    def add_food(self, quantity=0):
        self.food += quantity
        self.total_food += quantity

    def decrease_food(self, quantity=0):
        self.food -= quantity

    def get_animal_food(self):
        return self.animal_food

    def add_animal_food(self, quantity=0):
        self.animal_food += quantity

    def decrease_animal_food(self, quantity=0):
        self.animal_food -= quantity

    def get_money(self):
        return self.money

    def add_money(self, quantity=0):
        self.money += quantity

    def decrease_money(self, quantity=0):
        self.money -= quantity

    def get_debris(self):
        return self.debris

    def add_debris(self, quantity=0):
        self.debris += quantity

    def house_clearning(self, quantity=0):
        self.debris -= quantity

    def add_cat(self, new_cat=None):
        self.list_cats.append(new_cat)
        self.quantity_cats += 1

    def get_cat_by_number(self, number_cat=0):
        return self.list_cats[number_cat]

    def get_quantity_cats(self):
        return self.quantity_cats


class Human:

    def __init__(self):
        self.fullness = 50
        self.happiness = 0
        self.house = None
        self.living = True
        self.stroking_cat = False

    def __str__(self):
        return 'сытость  {}, степень счастья  {}'.format(
            self.fullness, self.happiness)

    def is_living(self):
        return self.living


class Husband(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.quantity_tanks = 0
        self.total_salary = 0
        self.salary = 150
        self.wife = None
        self.quarrel_with_wife = False

    def __str__(self):
        return 'Я муж {}, у меня танков  {}, '.format(
            self.name, self.quantity_tanks) + super().__str__()

    def set_quarrel_with_wife(self):
        self.quarrel_with_wife = True

    def marriage(self, wife):
        self.wife = wife
        self.happiness += 100
        cprint('{} женился на {}'.format(self.name, self.wife.name), color='blue')

    def settle_in_house(self, house):
        self.house = house
        cprint('{} поселился в доме'.format(self.name), color='blue')

    def eat(self):
        if self.house.get_food() >= 30:
            cprint('{} поел'.format(self.name), color='blue')
            self.fullness += 30
            self.house.decrease_food(quantity=30)
            self.happiness += 5
        else:
            cprint('{} хотел поесть, но у него нет еды'.format(self.name), color='blue')
            self.fullness -= 10
            self.happiness -= 5

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.add_money(quantity=self.salary)
        self.total_salary += self.salary
        self.fullness -= 10
        self.happiness += 5

    def gaming(self):
        cprint('{} играл в WoT целый день'.format(self.name), color='blue')
        serge.quantity_tanks += 1
        self.fullness -= 10
        self.happiness += 20

    def quarrel(self):
        self.fullness -= 10
        self.happiness -= 10
        self.house.get_cat_by_number(number_cat=0).set_stroking_cat(name_owner=self.name)
        cat_name = self.house.get_cat_by_number(number_cat=0).get_cat_name()
        cprint('{} скандалил с женой и для успокоения гладил кота {}!'.format(
            self.name, cat_name), color='yellow')

    def act(self):
        if self.living:
            if self.fullness < 0 or self.happiness < 10:
                cprint('{} умер...'.format(self.name), color='red')
                self.living = False
                return
            if self.quarrel_with_wife:
                self.quarrel()
                self.quarrel_with_wife = False
            elif self.fullness <= 10:
                self.eat()
            elif self.house.get_money() <= 350:
                self.work()
            else:
                self.gaming()
        else:
            cprint('==================', color='red')


class Wife(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.quantity_fur = 0
        self.quantity_quarrel = 0
        self.husband = None
        self.quarrel_with_husband = False

    def __str__(self):
        return 'Я жена {}, у меня шуб {}, '.format(
            self.name, self.quantity_fur) + super().__str__()

    def marriage(self, husband):
        self.husband = husband
        self.happiness += 100
        cprint('{} вышла замуж за {}'.format(self.name, self.husband.name), color='cyan')

    def settle_in_house(self, house):
        self.house = house
        cprint('{} поселилась в доме'.format(self.name), color='cyan')

    def eat(self):
        if self.house.get_food() >= 30:
            cprint('{} поела'.format(self.name), color='cyan')
            self.fullness += 30
            self.house.decrease_food(quantity=30)
            self.happiness += 30
        else:
            cprint('{} хотела поесть, но у нее нет еды'.format(self.name), color='cyan')
            self.fullness -= 10
            self.happiness -= 5
            self.shopping()

    def shopping(self):
        if self.house.get_money() >= 70:
            cprint('{} сходила в магазин за едой'.format(self.name), color='cyan')
            self.house.decrease_money(quantity=70)
            self.house.add_food(quantity=50)
            self.house.add_animal_food(quantity=20)
            self.fullness -= 10
            self.happiness -= 5

        else:
            cprint('{} хотела пойти за продуктами, но не хватает денег!'.format(
                self.name), color='cyan')
            self.fullness -= 10
            self.happiness -= 5

    def shopping_fur(self):
        if self.house.get_money() >= 400:
            cprint('{} купила {} шубу!'.format(
                self.name, self.quantity_fur + 1), color='cyan')
            self.house.decrease_money(quantity=350)
            self.happiness += 60
            self.fullness -= 10
            self.quantity_fur += 1
        else:
            cprint('{} хотела купить шубу, но не хватило денег на {} шубу!'.format(
                self.name, self.quantity_fur + 1), color='cyan')
            self.fullness -= 10
            self.happiness -= 20

    def clearn_house(self):
        self.house.house_clearning(100)
        self.fullness -= 10
        self.happiness -= 15
        cprint('{} убиралась в доме'.format(self.name), color='cyan')

    def quarrel(self):
        self.quantity_quarrel += 1
        self.fullness -= 10
        self.happiness -= 30
        self.quarrel_with_husband = True
        self.husband.set_quarrel_with_wife()
        cprint('{} закатила скандал, так как не хватает денег на покупку {} шубы!'.format(
            self.name, self.quantity_fur + 1), color='cyan')

    def act(self):
        if self.living:
            dice = randint(1, 6)
            if self.fullness < 0 or self.happiness < 10:
                cprint('{} умерла...'.format(self.name), color='red')
                self.living = False
                return
            if self.fullness <= 10:
                self.eat()
            elif self.house.get_food() <= 30 or self.house.get_animal_food() <= 0:
                self.shopping()
            elif self.house.get_debris() >= 100:
                self.clearn_house()
            elif dice == 1 and self.house.get_money() < 400 and self.husband.is_living():
                self.quarrel()
                self.quarrel_with_husband = False
            else:
                self.shopping_fur()
        else:
            cprint('==================', color='red')


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None
        self.living = True
        self.stroking_cat = False
        self.name_owner = None

    def __str__(self):
        if self.living:
            if self.fullness < 0:
                cprint('Кот {} умер...'.format(self.name), color='red')
                self.living = False

            str_print = 'Я кот - {}, сытость {}'.format(self.name, self.fullness)
        else:
            str_print = '========================='
        return str_print

    def set_stroking_cat(self, name_owner=None):
        self.stroking_cat = True
        self.name_owner = name_owner

    def get_cat_name(self):
        return self.name

    def stroking(self):
        cprint('Кота {} гладил {} целый день'.format(self.name, self.name_owner), color='magenta')
        self.stroking_cat = False

    def settle_in_house(self, house):
        self.house = house
        cprint('Кот {} поселился в доме'.format(self.name), color='magenta')

    def eat(self):
        if self.house.get_animal_food() >= 10:
            cprint('Кот {} поел'.format(self.name), color='magenta')
            self.fullness += 10
            self.house.decrease_animal_food(quantity=10)
        else:
            self.fullness -= 10
            cprint('У кота {} нет еды. Остался голодный на всесь день'.format(self.name), color='magenta')

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} дрых весь день'.format(self.name), color='magenta')

    def strip_wallpaper(self):
        self.fullness -= 10
        self.house.add_debris(quantity=5)
        cprint('Кот {} подрал обои'.format(self.name), color='magenta')

    def act(self):
        if self.living:
            dice = randint(1, 6)
            if self.stroking_cat:
                self.stroking()
            elif self.fullness < 20:
                self.eat()
            elif dice in (1, 3, 5):
                self.sleep()
            else:
                self.strip_wallpaper()
        else:
            cprint('=======================', color='red')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
cat = Cat(name='Мурзик')
serge.marriage(wife=masha)
masha.marriage(husband=serge)
serge.settle_in_house(house=home)
masha.settle_in_house(house=home)
cat.settle_in_house(house=home)
home.add_cat(new_cat=cat)


for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    masha.act()
    serge.act()
    cat.act()
    home.act()
    cprint('---------------------------------------------'.format(day), color='white')
    cprint(masha, color='cyan')
    cprint(serge, color='blue')
    cprint(cat, color='magenta')
    cprint(home, color='white')

cprint('================== Итог жизни за {} дней ============'.format(day), color='yellow')
cprint(masha, color='yellow')
cprint(serge, color='yellow')
cprint(cat, color='yellow')
cprint('{} закатила за {} дней {} скандалов'.format(masha.name, day, masha.quantity_quarrel), color='red')
cprint('{} заработал за {} дней {} баксов'.format(serge.name, day, serge.total_salary), color='red')
cprint('И ими было съедено {} еды'.format(home.total_food), color='red')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass
#

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу
# над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#
# # TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')
#

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

