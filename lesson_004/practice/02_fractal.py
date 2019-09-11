# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rand

sd.resolution = (800, 800)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(400, 5)


# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
def branch(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point


# angle_0 = 90
# length_0 = 200
# next_point = branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)
# next_angle = next_angle - 30
# next_length = next_length * .75
# next_point = branch(point=next_point, angle=next_angle, length=next_length)


# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов
# angle_0 = 90
# length_0 = 200
#
# next_angle = angle_0
# next_length = length_0
# next_point = point_0
#
#
# while next_length > 1:
#     next_point = branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle = next_angle - 30
#     next_length = next_length * 0.75


# сделать функцию branch рекурсивной

# def branch(point, angle, length, delta):
#     if length < 1:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * 0.75
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)
#
#
# for delta in range(0, 51, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)


# # Веточки рисует симметричные, похожие на образец
# def branch(point, angle, length):
#     if length < 4:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle + 25, length=length, width=1)
#     v2 = sd.get_vector(start_point=point, angle=angle - 25, length=length, width=1)
#     v1.draw()
#     v2.draw()
#     next_point1 = v1.end_point
#     next_point2 = v2.end_point
#     next_angle1 = angle + 27
#     next_angle2 = angle - 27
#     next_length = length * 0.75
#     branch(point=next_point1, angle=next_angle1, length=next_length)
#     branch(point=next_point2, angle=next_angle2, length=next_length)
#
# # Вызов процедуры с веточкими
# branch(point=point_0, angle=90, length=140)
#



sd.pause()

