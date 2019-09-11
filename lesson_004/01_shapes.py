# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# def triangle_first_edition(point=sd.get_point(0, 0), angle=0, length=100):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle= angle + 240, length=length, width=3)
#     v3.draw()


# # Вызов функции
# start_point = sd.get_point(300, 300)
# angle = 25
# length = 235
# triangle_first_edition(point=start_point, angle=angle, length=length)
# #===============================================================================================================

# # Рефакторим код: вводим цикл
# def triangle_second_edition(point=sd.get_point(0, 0), angle=0, length=100):
#     first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     first_vector.draw()
#     next_vector = first_vector
#     for i in range(2):
#         angle += 120
#         next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
#         next_vector.draw()
#
#
# # Вызов функции
# start_point = sd.get_point(250, 250)
# angle = 23
# length = 272
# triangle_second_edition(point=start_point, angle=angle, length=length)
# #===============================================================================================================


# # Рефакторим код далее: устраняем разрыв в будущих фигурах условием достижения последней грани,
# # которую рисуем линией
# def triangle_third_edition(point=sd.get_point(0, 0), angle=0, length=100):
#     first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     first_vector.draw()
#     next_vector = first_vector
#     for i in range(2):
#         if i == 1:
#             sd.line(start_point=next_vector.end_point, end_point=point)
#         else:
#             angle += 120
#             next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
#             next_vector.draw()
#
#
# # Вызов функции
# start_point = sd.get_point(150, 150)
# angle = 45
# length = 287
# triangle_third_edition(point=start_point, angle=angle, length=length)
#
# Навороты из закрученных треугольников
# length_vector = 150
# angle = 0
# center_vector = sd.get_point(300, 300)
# length_draw = 100
# for angle_vector in range(0, 361, 30):
#     draw_line = sd.get_vector(start_point=center_vector, angle=angle_vector, length=length_vector, width=1)
#     angle_vector += 30
#     center_draw = draw_line.end_point
#     for angle in range(0, 361, 20):
#         triangle(point=center_draw, angle=angle, length=length_draw)
# # ===============================================================================================================


# # Рефакторим код далее: делаем задел для построения многоугольников, вводим параметр количество углов
# def triangle_fourth_edition(point=sd.get_point(0, 0), angle=0, length=100, corner=3):
#     first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     first_vector.draw()
#     next_vector = first_vector
#     for i in range(corner - 1):
#         if i == corner - 2:
#             sd.line(start_point=next_vector.end_point, end_point=point)
#         else:
#             angle += int(360 / corner)
#             next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
#             next_vector.draw()
#
#
# # Вызов функции
# start_point = sd.get_point(175, 175)
# angle = 49
# length = 302
# triangle_fourth_edition(point=start_point, angle=angle, length=length, corner=3)
#
# #===============================================================================================================


# # Наслаждаемся жизнью, строим любые равносторонние многоугольники
def polygon(point=sd.get_point(0, 0), angle=0, length=100, corner=3):
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


# # Вызов функции
# start_point = sd.get_point(300, 200)
# angle = 0
# length = 50
# polygon(point=start_point, angle=angle, length=length, corner=8)
#
# # ===============================================================================================================


def square(point=sd.get_point(0, 0), angle=0, length=100):
    polygon(point=point, angle=angle, length=length, corner=4)


def pentagon(point=sd.get_point(0, 0), angle=0, length=100):
    polygon(point=point, angle=angle, length=length, corner=5)


def hexagon(point=sd.get_point(0, 0), angle=0, length=100):
    polygon(point=point, angle=angle, length=length, corner=6)


# Вызов функций
start_point = sd.get_point(300, 200)
angle = 0
length = 150
polygon(point=start_point, angle=angle, length=length, corner=3)
square(point=start_point, angle=angle, length=length)
pentagon(point=start_point, angle=angle, length=length)
hexagon(point=start_point, angle=angle, length=length)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
