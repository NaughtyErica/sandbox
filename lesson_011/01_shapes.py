# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n=3):
    def polygon(point=sd.get_point(0, 0), angle=0, length=100):
        corner = n
        first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        first_vector.draw()
        next_vector = first_vector
        for i in range(corner - 1):
            if i == corner - 2:
                sd.line(start_point=next_vector.end_point, end_point=point)
            else:
                angle += int(360 / corner)
                next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
                next_vector.draw()
    return polygon


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)
sd.pause()
