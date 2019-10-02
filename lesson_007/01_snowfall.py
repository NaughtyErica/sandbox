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

    def __del__(self):
        Snowflake.quantity_snow_flakes -= 1


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
        for i in range(quantity):
            Snowflake.list_snow_flakes.append(cls())






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

sd.pause()
