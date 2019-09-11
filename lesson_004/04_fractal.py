# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rand
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# def draw_branches(start_point, angle, length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length, width=1)
#     v2 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length, width=1)
#     v1.draw()
#     v2.draw()
#
#
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)
# ===========================================================================================

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# def draw_branches(start_point, angle, length):
#     if length < 8:
#         return
#     v1 = sd.get_vector(start_point=start_point, angle=angle + 20, length=length, width=1)
#     v2 = sd.get_vector(start_point=start_point, angle=angle - 20, length=length, width=1)
#     v1.draw()
#     v2.draw()
#     next_point1 = v1.end_point
#     next_point2 = v2.end_point
#     next_angle1 = angle + 20
#     next_angle2 = angle - 20
#     next_length = length * 0.8
#     draw_branches(start_point=next_point1, angle=next_angle1, length=next_length)
#     draw_branches(start_point=next_point2, angle=next_angle2, length=next_length)
#
#
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=105)
# # ===========================================================================================

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


def draw_branches_rand(start_point, angle, length):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle + sd.random_number(15, 25), length=length, width=1)
    v2 = sd.get_vector(start_point=start_point, angle=angle - sd.random_number(15, 25), length=length, width=1)
    v1.draw()
    v2.draw()
    next_point1 = v1.end_point
    next_point2 = v2.end_point
    next_angle1 = angle + sd.random_number(15, 25)
    next_angle2 = angle - sd.random_number(15, 25)
    random_number = rand.random()
    if random_number < 0.25:
        next_length = length * (0.72 + random_number)
    elif random_number > 0.75:
        next_length = length * (0.9 * random_number)
    else:
        next_length = length * 0.6

    draw_branches_rand(start_point=next_point1, angle=next_angle1, length=next_length)
    draw_branches_rand(start_point=next_point2, angle=next_angle2, length=next_length)


root_point = sd.get_point(300, 30)
draw_branches_rand(start_point=root_point, angle=90, length=120)
# ===========================================================================================


sd.pause()


