import simple_draw as sd
import random as rd
import pygame


# Класс снежинки для варианта одиночно падающей снежинки и трех вариантов снегопада
# class Snowflake:
#
#     def __init__(self, resolution=(1200, 600), len_beam_min_max=(15, 20)):
#         lst_factor = [[0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8],
#                       [0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45],
#                       [50, 52, 55, 57, 60, 62, 65, 67, 70],
#                       ]
#         coord_x = (-100, resolution[0] + 100)
#         coord_y = (resolution[1] + 70, resolution[1] * 2)
#         self.x = sd.random_number(coord_x[0], coord_x[1])
#         self.y = sd.random_number(coord_y[0], coord_y[1])
#         self.len_beam = sd.random_number(len_beam_min_max[0], len_beam_min_max[1])
#         self.factor_a = rd.choice(lst_factor[0])
#         self.factor_b = rd.choice(lst_factor[1])
#         self.factor_c = rd.choice(lst_factor[2])
#
#     def draw(self, color=sd.COLOR_WHITE):
#         if (-70 < self.x < 1270) and self.y < 700:
#             point = sd.get_point(self.x, self.y)
#             sd.snowflake(center=point, length=self.len_beam, color=color,
#                          factor_a=self.factor_a,
#                          factor_b=self.factor_b,
#                          factor_c=self.factor_c)
#
#     def shift_coord(self):
#         self.x += sd.random_number(-10, 10)
#         self.y -= sd.random_number(10, 20)
#

# Вариант одиночной падающей снежинки
# resolution_screen = sd.resolution = (1200, 600)
# flake = Snowflake()
# while True:
#     sd.start_drawing()
#     flake.draw(color=sd.background_color)
#     flake.shift_coord()
#     flake.draw(color=sd.COLOR_WHITE)
#     if flake.y < 0 - 35:
#         del flake
#         flake = Snowflake()
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# Вариант снегопада без глобальных переменных и функций
# count = 20
# resolution_screen = sd.resolution = (1200, 600)
# lst_flakes = []
# for fl in range(count):
#     flake = Snowflake()
#     lst_flakes.append(flake)
#
# while True:
#     for flake in lst_flakes:
#         sd.start_drawing()
#         flake.draw(color=sd.background_color)
#         flake.shift_coord()
#         flake.draw(color=sd.COLOR_WHITE)
#     lst_number_fallen_flakes = []
#     for fl in range(len(lst_flakes)):
#         if lst_flakes[fl].y < 0 - 35:
#             lst_number_fallen_flakes.append(fl)
#     quantity_delete = len(lst_number_fallen_flakes)
#     if quantity_delete > 0:
#         for fl in range(quantity_delete):
#             del lst_flakes[lst_number_fallen_flakes[fl]]
#             flake = Snowflake()
#             lst_flakes.insert(lst_number_fallen_flakes[fl], flake)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# Вариант снегопада с использванием функций без глобальных переменных
# def get_flakes(count=20):
#     list_snow_flakes = []
#     for fl in range(count):
#         flake = Snowflake()
#         list_snow_flakes.append(flake)
#     return list_snow_flakes
#
#
# def get_number_fallen_flakes(lst_snow_flakes=[]):
#     list_number_fallen_flakes = []
#     for fl in range(len(lst_snow_flakes)):
#         if lst_snow_flakes[fl].y < 0 - 35:
#             list_number_fallen_flakes.append(fl)
#     return list_number_fallen_flakes
#
#
# def append_flakes_instead_fallen(lst_number_fallen_flakes=[], lst_snow_flakes=[]):
#     quantity_delete = len(lst_number_fallen_flakes)
#     if quantity_delete > 0:
#         for fl in range(quantity_delete):
#             del lst_snow_flakes[lst_number_fallen_flakes[fl]]
#             flake = Snowflake()
#             lst_snow_flakes.insert(lst_number_fallen_flakes[fl], flake)
#
#
# resolution_screen = sd.resolution = (1200, 600)
# lst_flakes = get_flakes(count=20)
# while True:
#     for flake in lst_flakes:
#         sd.start_drawing()
#         flake.draw(color=sd.background_color)
#         flake.shift_coord()
#         flake.draw(color=sd.COLOR_WHITE)
#     l_number_fallen_flakes = get_number_fallen_flakes(lst_snow_flakes=lst_flakes)
#     append_flakes_instead_fallen(lst_number_fallen_flakes=l_number_fallen_flakes, lst_snow_flakes=lst_flakes)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# Вариант снегопада с применением глобальных переменных для работы функций
# resolution_screen = sd.resolution = (1200, 600)
# list_snow_flakes = []
# list_number_fallen_flakes = []
# quantity_snow_flakes = 20
#
#
# def get_flakes(count=20):
#     global list_snow_flakes
#     for fl in range(count):
#         flake = Snowflake()
#         list_snow_flakes.append(flake)
#     return list_snow_flakes
#
#
# def get_number_fallen_flakes():
#     global list_number_fallen_flakes
#     list_number_fallen_flakes = []
#     for fl in range(quantity_snow_flakes):
#         if list_snow_flakes[fl].y < 0 - 35:
#             list_number_fallen_flakes.append(fl)
#     return list_number_fallen_flakes
#
#
# def append_flakes_instead_fallen():
#     global list_number_fallen_flakes
#     quantity_delete = len(list_number_fallen_flakes)
#     if quantity_delete > 0:
#         for fl in range(quantity_delete):
#             del list_snow_flakes[list_number_fallen_flakes[fl]]
#             flake = Snowflake()
#             list_snow_flakes.insert(list_number_fallen_flakes[fl], flake)
#
#
# lst_flakes = get_flakes(count=quantity_snow_flakes)
# while True:
#     for flake in lst_flakes:
#         sd.start_drawing()
#         flake.draw(color=sd.background_color)
#         flake.shift_coord()
#         flake.draw(color=sd.COLOR_WHITE)
#     get_number_fallen_flakes()
#     append_flakes_instead_fallen()
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# Класс снежинки для использоаания в классе снегопада
class Snowflake:

    def __init__(self, resolution=(1200, 600), len_beam_min_max=(15, 20)):
        lst_factor = [[0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8],
                      [0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45],
                      [50, 52, 55, 57, 60, 62, 65, 67, 70],
                     ]
        coord_x = (-100, resolution[0] + 100)
        coord_y = (resolution[1] + 70, resolution[1] * 2)
        self.x = sd.random_number(coord_x[0], coord_x[1])
        self.y = sd.random_number(coord_y[0], coord_y[1])
        self.len_beam = sd.random_number(len_beam_min_max[0], len_beam_min_max[1])
        self.factor_a = rd.choice(lst_factor[0])
        self.factor_b = rd.choice(lst_factor[1])
        self.factor_c = rd.choice(lst_factor[2])

    def draw_snow_flake(self, color=sd.COLOR_WHITE):
        """
            factor_a=0.6, factor_b=0.35, factor_c=60
            factor_a - место ответвления лучиков
            factor_b - длина лучиков
            factor_c - угол отклонения лучиков
        """
        if (-70 < self.x < 1270) and self.y < 700:
            point = sd.get_point(self.x, self.y)
            sd.snowflake(center=point, length=self.len_beam, color=color,
                         factor_a=self.factor_a,
                         factor_b=self.factor_b,
                         factor_c=self.factor_c)

    def shift_coord_snow_flake(self, wind_direction=0):
        self.x += sd.random_number(-10, 10) + wind_direction * 20
        self.y -= sd.random_number(10, 20)


# Класс снегопада с использованием класса снежинки
class SnowFall:

    def __init__(self, quantity_snow_flakes=0):
        self.quantity_flakes = quantity_snow_flakes
        self.list_snow_flakes = []
        self.number_fallen_flakes = []
        self.wind_direction = 0
        for fl in range(self.quantity_flakes):
            flake = Snowflake()
            self.list_snow_flakes.append(flake)

    def insert_to_list_snow_flakes(self, count=0):
        for fl in range(count):
            flake = Snowflake()
            self.quantity_flakes += 1
            self.list_snow_flakes.append(flake)

    def get_fallen_flakes(self):
        self.number_fallen_flakes = []
        for fl in range(self.quantity_flakes):
            if self.list_snow_flakes[fl].y < 0 - 35:
                self.number_fallen_flakes.append(fl)

    def delete_fallen_create_new(self):
        quantity_delete = len(self.number_fallen_flakes)
        if quantity_delete > 0:
            for fl in range(quantity_delete):
                del self.list_snow_flakes[self.number_fallen_flakes[fl]]
                flake = Snowflake()
                self.list_snow_flakes.insert(self.number_fallen_flakes[fl], flake)

    def draw_all_snow_flakes(self, color=sd.COLOR_WHITE):
        for fl in range(self.quantity_flakes):
            self.list_snow_flakes[fl].draw_snow_flake(color=color)

    def install_wind(self, direction=0):
        self.wind_direction = direction

    def shift_all_snow_flakes(self):
        for fl in range(self.quantity_flakes):
            self.list_snow_flakes[fl].shift_coord_snow_flake(wind_direction=self.wind_direction)
        self.wind_direction = 0

    def thin_snow(self):
        number_snowflake_upper = []
        for fl in range(self.quantity_flakes):
            if self.list_snow_flakes[fl].y > 800:
                number_snowflake_upper.append(fl)
        count_upper = len(number_snowflake_upper)
        if count_upper > 0:
            del self.list_snow_flakes[number_snowflake_upper[0]]
            self.quantity_flakes -= 1

    def get_quantity_flakes(self):
        return self.quantity_flakes


resolution_screen = sd.resolution = (1200, 600)
snow_fall = SnowFall(quantity_snow_flakes=40)
print("Усиление снегопада - S\n"
      "Уменьшение снегопада - W\n"
      "Ветер справа - A\n"
      "Ветер слева - D\n"
      "Клавиши нажимать дробно. Усиление +5 снежинок, уменьшение -1")
while True:
    sd.start_drawing()
    snow_fall.draw_all_snow_flakes(color=sd.background_color)
    snow_fall.shift_all_snow_flakes()
    snow_fall.draw_all_snow_flakes(color=sd.COLOR_WHITE)
    snow_fall.get_fallen_flakes()
    snow_fall.delete_fallen_create_new()
    sd.finish_drawing()
    keyState = pygame.key.get_pressed()
    if keyState[pygame.K_s]:
        snow_fall.insert_to_list_snow_flakes(count=5)
    if keyState[pygame.K_w]:
        snow_fall.thin_snow()
    if keyState[pygame.K_a]:
        snow_fall.install_wind(direction=-1)
    if keyState[pygame.K_d]:
        snow_fall.install_wind(direction=1)
    sd.sleep(0.1)
    if sd.user_want_exit() or snow_fall.get_quantity_flakes() > 200:
        break
sd.pause()
sd.pause()

# Снегопад через методы класса снежинка
# class Snowflake:
#     quantity_snow_flakes = 0
#     wind_direction = 0
#     list_snow_flakes = []
#     number_snowflake_bottom = []
#
#     def __init__(self, resolution=(1200, 600), len_beam_min_max=(15, 20)):
#         self.center_and_beams_snowflake = []
#
#         self.lst_factor = [[0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8],
#                            [0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45],
#                            [50, 52, 55, 57, 60, 62, 65, 67, 70],
#                            ]
#         coord_x = (-100, resolution[0] + 100)
#         coord_y = (resolution[1] + 70, resolution[1] * 2)
#         x = sd.random_number(coord_x[0], coord_x[1])
#         y = sd.random_number(coord_y[0], coord_y[1])
#         len_beam = sd.random_number(len_beam_min_max[0], len_beam_min_max[1])
#         factor_a = rd.choice(self.lst_factor[0])
#         factor_b = rd.choice(self.lst_factor[1])
#         factor_c = rd.choice(self.lst_factor[2])
#         self.center_and_beams_snowflake.append(x)
#         self.center_and_beams_snowflake.append(y)
#         self.center_and_beams_snowflake.append(len_beam)
#         self.center_and_beams_snowflake.append(factor_a)
#         self.center_and_beams_snowflake.append(factor_b)
#         self.center_and_beams_snowflake.append(factor_c)
#         Snowflake.quantity_snow_flakes += 1
#
#     def draw_snow_flake(self, color=sd.COLOR_WHITE):
#         """
#             factor_a=0.6, factor_b=0.35, factor_c=60
#             factor_a - место ответвления лучиков
#             factor_b - длина лучиков
#             factor_c - угол отклонения лучиков
#         """
#         if (-70 < self.center_and_beams_snowflake[0] < 1270) and self.center_and_beams_snowflake[1] < 700:
#             point = sd.get_point(self.center_and_beams_snowflake[0], self.center_and_beams_snowflake[1])
#             sd.snowflake(center=point, length=self.center_and_beams_snowflake[2], color=color,
#                          factor_a=self.center_and_beams_snowflake[3],
#                          factor_b=self.center_and_beams_snowflake[4],
#                          factor_c=self.center_and_beams_snowflake[5])
#
#     def shift_coord_snow_flake(self):
#         self.center_and_beams_snowflake[0] += sd.random_number(-10, 10) + Snowflake.wind_direction * 20
#         self.center_and_beams_snowflake[1] -= sd.random_number(10, 20)
#
#     @classmethod
#     def create_list_snow_flakes(cls, quantity=0):
#         for fl in range(quantity):
#             Snowflake.list_snow_flakes.append(cls())
#
#     @classmethod
#     def insert_to_list_snow_flakes(cls, position=0):
#         Snowflake.list_snow_flakes.insert(position, cls())
#
#     @classmethod
#     def list_flown_bottom(cls):
#         Snowflake.wind_direction = 0
#         Snowflake.number_snowflake_bottom = []
#         for fl in range(Snowflake.quantity_snow_flakes):
#             if Snowflake.list_snow_flakes[fl].center_and_beams_snowflake[1] < 0 - 35:
#                 Snowflake.number_snowflake_bottom.append(fl)
#         return Snowflake.number_snowflake_bottom
#
#     @classmethod
#     def delete_flown_bottom(cls):
#         quantity_delete = len(Snowflake.number_snowflake_bottom)
#         if quantity_delete > 0:
#             for fl in range(quantity_delete):
#                 del Snowflake.list_snow_flakes[Snowflake.number_snowflake_bottom[fl]]
#                 Snowflake.quantity_snow_flakes -= 1
#                 Snowflake.list_snow_flakes.insert(Snowflake.number_snowflake_bottom[fl], cls())
#
#     @classmethod
#     def draw_all_snow_flakes(cls, color=sd.COLOR_WHITE):
#         for fl in range(Snowflake.quantity_snow_flakes):
#             Snowflake.draw_snow_flake(Snowflake.list_snow_flakes[fl], color=color)
#
#     @classmethod
#     def shift_all_snow_flakes(cls):
#         for fl in range(Snowflake.quantity_snow_flakes):
#             Snowflake.shift_coord_snow_flake(Snowflake.list_snow_flakes[fl])
#
#     @classmethod
#     def wind(cls, direction=0):
#         Snowflake.wind_direction = direction
#
#     @classmethod
#     def thin_snow(cls):
#         number_snowflake_upper = []
#         for fl in range(Snowflake.quantity_snow_flakes):
#             if Snowflake.list_snow_flakes[fl].center_and_beams_snowflake[1] > 800:
#                 number_snowflake_upper.append(fl)
#         count_upper = len(number_snowflake_upper)
#         if count_upper > 0:
#             del Snowflake.list_snow_flakes[number_snowflake_upper[0]]
#             Snowflake.quantity_snow_flakes -= 1
#
#
# count_snow_flakes = 0
# resolution_screen = sd.resolution = (1200, 600)
# Snowflake.create_list_snow_flakes(quantity=20)
# print("Усиление снегопада - S")
# print("Уменьшение снегопада - W")
# print("Ветер справа - A")
# print("Ветер слева - D")
# print("Клавиши нажимать дробно. Усиление +5 снежинок, уменьшение -1")
# while True:
#     sd.start_drawing()
#     Snowflake.draw_all_snow_flakes(color=sd.background_color)
#     Snowflake.shift_all_snow_flakes()
#     Snowflake.draw_all_snow_flakes(color=sd.COLOR_WHITE)
#     Snowflake.list_flown_bottom()
#     Snowflake.delete_flown_bottom()
#     sd.finish_drawing()
#     keyState = pygame.key.get_pressed()
#     if keyState[pygame.K_s]:
#         Snowflake.create_list_snow_flakes(quantity=5)
#     if keyState[pygame.K_w]:
#         Snowflake.thin_snow()
#     if keyState[pygame.K_a]:
#         Snowflake.wind(direction=-1)
#     if keyState[pygame.K_d]:
#         Snowflake.wind(direction=1)
#     sd.sleep(0.1)
#     if sd.user_want_exit() or count_snow_flakes > 200:
#         break
# sd.pause()
