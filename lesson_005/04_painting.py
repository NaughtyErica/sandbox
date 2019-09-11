# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from lesson_005.draw_object import tree
from lesson_005.draw_object import house
from lesson_005.draw_object import rainbow
from lesson_005.draw_object import sun
from lesson_005.draw_object import clouds
from lesson_005.draw_object import snow_melts
from lesson_005.draw_object import smile
sd.resolution = (1200, 600)

bl = sd.get_point(300, 1)
tr = sd.get_point(660, 211)

N = 20
center_snowflake = []
length_beam = []
drift = 0
step_draw = 0
for i in range(N):
    coord_xy = []
    x = sd.random_number(-22, 278)
    y = sd.random_number(640, 1400)
    coord_xy.append(x)
    coord_xy.append(y)
    center_snowflake.append(coord_xy)
    length_beam.append(sd.random_number(15, 20))

house.draw_house(bottom_left=bl, top_right=tr, win_l=120, win_h=100, brick_l=60, brick_h=30)
smile.draw_smile(open_eye=1)
tree.draw_branches_rand(start_point=sd.get_point(1000, 1))

while True:
    sd.start_drawing()
    for i in range(N):
        if (-20 <= center_snowflake[i][0] <= 300) and drift < center_snowflake[i][1] < 640:
            point = sd.get_point(center_snowflake[i][0], center_snowflake[i][1])
            sd.snowflake(center=point, length=length_beam[i], color=sd.background_color)
            center_snowflake[i][0] += sd.random_number(-2, 2)
            if center_snowflake[i][0] > 280:
                center_snowflake[i][0] = 280
            center_snowflake[i][1] -= sd.random_number(2, 5)
            point = sd.get_point(center_snowflake[i][0], center_snowflake[i][1])
            sd.snowflake(center=point, length=length_beam[i])
        else:
            if drift < 20:
                center_snowflake[i][1] -= sd.random_number(2, 5)
        if center_snowflake[i][1] < drift < 20:
            x = sd.random_number(-22, 278)
            y = sd.random_number(640, 1200)
            center_snowflake[i][0] = x
            center_snowflake[i][1] = y
            length_beam[i] = sd.random_number(15, 25)

    clouds.draw_clouds()
    sun.draw_sun(center=sd.get_point(700 - step_draw // 10, 300 + step_draw // 10), length_ray=50 + drift * 2, color=sd.background_color)
    
    step_draw += 1
    if step_draw % 60 == 0:
        drift += 1

    sun.draw_sun(center=sd.get_point(700 - step_draw // 10, 300 + step_draw // 10), length_ray=50 + drift * 2, color=sd.COLOR_YELLOW)

    if drift == 20:
        center_rainbow = sd.get_point(400, -50)
        rainbow.draw_rainbow(center_point=center_rainbow, radius=800)
    if drift > 20:
        snow_melts.melts(depth=(drift - 20) * 2)
    if drift % 2 == 0:
        smile.draw_smile(open_eye=0)
    else:
        smile.draw_smile(open_eye=1)
    sd.finish_drawing()
    sd.sleep(0.02)
    if sd.user_want_exit() or drift > 40:
        break

sd.pause()


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
