# -*- coding: utf-8 -*-


import simple_draw as sd
import random as rd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    quantity_snow_flakes = 0
    wind_direction = 0
    list_snow_flakes = []
    number_snowflake_bottom = []

    def __init__(self, resolution=(1200, 600), len_beam_min_max=(15, 20)):
        self.center_and_beams_snowflake = []

        self.lst_factor = [[0.4, 0.5, 0.6, 0.7, 0.8],
                           [0.25, 0.3, 0.35, 0.4, 0.45],
                           [50, 55, 60, 65, 70],
                           ]
        # default value: factor_a=0.6, factor_b=0.35, factor_c=60
        coord_x = (-100, resolution[0] + 100)
        coord_y = (resolution[1] + 70, resolution[1] * 2)
        x = sd.random_number(coord_x[0], coord_x[1])
        y = sd.random_number(coord_y[0], coord_y[1])
        len_beam = sd.random_number(len_beam_min_max[0], len_beam_min_max[1])
        factor_a = rd.choice(self.lst_factor[0])
        factor_b = rd.choice(self.lst_factor[1])
        factor_c = rd.choice(self.lst_factor[2])
        self.center_and_beams_snowflake.append(x)
        self.center_and_beams_snowflake.append(y)
        self.center_and_beams_snowflake.append(len_beam)
        self.center_and_beams_snowflake.append(factor_a)
        self.center_and_beams_snowflake.append(factor_b)
        self.center_and_beams_snowflake.append(factor_c)
        Snowflake.quantity_snow_flakes += 1

    # def __del__(self, position=0):
    #     Snowflake.quantity_snow_flakes -= 1
    #     Snowflake.list_snow_flakes.pop(position)

    def draw_snow_flake(self, color=sd.COLOR_YELLOW):
        """
            factor_a=0.6, factor_b=0.35, factor_c=60
            factor_a - место ответвления лучиков
            factor_b - длина лучиков
            factor_c - угол отклонения лучиков
        """
        if (-70 < self.center_and_beams_snowflake[0] < 1270) and self.center_and_beams_snowflake[1] < 700:
            point = sd.get_point(self.center_and_beams_snowflake[0], self.center_and_beams_snowflake[1])
            sd.snowflake(center=point, length=self.center_and_beams_snowflake[2], color=color,
                         factor_a=self.center_and_beams_snowflake[3],
                         factor_b=self.center_and_beams_snowflake[4],
                         factor_c=self.center_and_beams_snowflake[5])

    def shift_coord_snow_flake(self):
        self.center_and_beams_snowflake[0] += sd.random_number(-10, 10) + Snowflake.wind_direction * 20
        self.center_and_beams_snowflake[1] -= sd.random_number(10, 20)

    @classmethod
    def create_list_snow_flakes(cls, quantity=0):
        Snowflake.quantity_snow_flakes = quantity
        for fl in range(quantity):
            Snowflake.list_snow_flakes.append(cls())

    @classmethod
    def insert_to_list_snow_flakes(cls, position=0):
        Snowflake.list_snow_flakes.insert(position, cls())

    @classmethod
    def list_flown_bottom(cls):
        Snowflake.number_snowflake_bottom = []
        for fl in range(Snowflake.quantity_snow_flakes):
            if Snowflake.list_snow_flakes[fl][1] < 0 - 35:
                Snowflake.number_snowflake_bottom.append(fl)
        return Snowflake.number_snowflake_bottom

    @classmethod
    def delete_flown_bottom(cls):
        quantity_delete = len(Snowflake.number_snowflake_bottom)
        if quantity_delete > 0:
            for fl in range(quantity_delete):
                del Snowflake.list_snow_flakes[Snowflake.number_snowflake_bottom[fl]]
                Snowflake.list_snow_flakes.insert(Snowflake.number_snowflake_bottom[fl], cls())

    @classmethod
    def draw_all_snow_flakes(cls, color=sd.COLOR_YELLOW):
        for fl in range(Snowflake.quantity_snow_flakes):
            cls.draw_snow_flake()


    # def del_snow_flake(self, number_snow_flake=0):
    #     center_and_beams_snowflake.pop(number_snow_flake)
    #     quantity_snow_flakes -= 1


    # def thin_snow():
    #     number_snowflake_upper = []
    #     for i in range(quantity_snow_flakes):
    #         if center_and_beams_snowflakes[i][1] > 800:
    #             number_snowflake_upper.append(i)
    #     count_upper = len(number_snowflake_upper)
    #     if count_upper > 0:
    #         center_and_beams_snowflakes.pop(number_snowflake_upper[0])
    #         quantity_snow_flakes -= 1
    #     print("Осталось снежинок", quantity_snow_flakes)
    #
    #
    # def list_flown_bottom():
    #     number_snowflake_bottom = []
    #     wind_direction = 0
    #     for i in range(quantity_snow_flakes):
    #         if center_and_beams_snowflakes[i][1] < 0 - 35:
    #             number_snowflake_bottom.append(i)
    #     return number_snowflake_bottom
    #
    #
    # def wind(direction=0):
    #     wind_direction = direction
    #     # Так проще использовать функцию
    #     if direction > 0:
    #         print("Ветер слева")
    #     elif direction < 0:
    #         print("Ветер справа")

# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

count_snow_flakes = 0
resolution_screen = sd.resolution = (1200, 600)
Snowflake.create_list_snow_flakes(quantity=20)
# print("Усиление снегопада - S")
# print("Уменьшение снегопада - W")
# print("Ветер справа - A")
# print("Ветер слева - D")
# print("Клавиши нажимать дробно. Усиление +5 снежинок, уменьшение -1")
while True:
    sd.start_drawing()
    snow.draw_snow_flakes(color=sd.background_color)
    snow.shift_coord_snow_flakes()
    snow.draw_snow_flakes(color=sd.COLOR_WHITE)
    lst_bottom = snow.list_flown_bottom()
    quantity_deleted = len(lst_bottom)
    if quantity_deleted > 0:
        for i in range(quantity_deleted):
            snow.del_snow_flake(number_snow_flake=lst_bottom[i])
            snow.create_snowflakes_pos(quantity=1, position_add=lst_bottom[i], resolution=resolution_screen)
    sd.finish_drawing()
    # В таком вариант у меня устойчиво ловит команды клавиатуры, правда иногда дублирует их
    # а в предыдущем варианте почти не работало
    keyState = pygame.key.get_pressed()
    if keyState[pygame.K_s]:
        count_snow_flakes = snow.create_snowflakes(quantity=5, resolution=resolution_screen)
    if keyState[pygame.K_w]:
        snow.thin_snow()
    if keyState[pygame.K_a]:
        snow.wind(direction=-1)
    if keyState[pygame.K_d]:
        snow.wind(direction=1)
    sd.sleep(0.1)
    if sd.user_want_exit() or count_snow_flakes > 200:
        break
sd.pause()

