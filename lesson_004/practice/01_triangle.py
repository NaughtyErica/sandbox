# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd


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
#             sd.line(next_vector.end_point, point)
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
# def triangle_third_edition(point=sd.get_point(0, 0), angle=0, length=100, corner=3):
#     first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     first_vector.draw()
#     next_vector = first_vector
#     for i in range(corner - 1):
#         if i == corner - 2:
#             sd.line(next_vector.end_point, point)
#         else:
#             angle += 360 / corner
#             next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
#             next_vector.draw()
#
#
# # Вызов функции
# start_point = sd.get_point(175, 175)
# angle = 49
# length = 302
# triangle_third_edition(point=start_point, angle=angle, length=length, corner=3)
#
# #===============================================================================================================

# # Наслаждаемся жизнью, строим любые равносторонние многоугольники
# def polygon(point=sd.get_point(0, 0), angle=0, length=100, corner=3):
#     first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     first_vector.draw()
#     next_vector = first_vector
#     for i in range(corner - 1):
#         if i == corner - 2:
#             sd.line(next_vector.end_point, point)
#         else:
#             angle += int(360 / corner)
#             next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
#             next_vector.draw()
#
#
# # Вызов функции
# start_point = sd.get_point(300, 200)
# angle = 0
# length = 50
# polygon(point=start_point, angle=angle, length=length, corner=8)
#
# # ===============================================================================================================


# def square(point=sd.get_point(0, 0), angle=0, length=100):
#     polygon(point=point, angle=angle, length=length, corner=4)
#
#
# def pentagon(point=sd.get_point(0, 0), angle=0, length=100):
#     polygon(point=point, angle=angle, length=length, corner=5)
#
#
# def hexagon(point=sd.get_point(0, 0), angle=0, length=100):
#     polygon(point=point, angle=angle, length=length, corner=6)
#
#
# # Вызов функций
# start_point = sd.get_point(300, 200)
# angle = 0
# length = 150
# polygon(point=start_point, angle=angle, length=length, corner=3)
# square(point=start_point, angle=angle, length=length)
# pentagon(point=start_point, angle=angle, length=length)
# hexagon(point=start_point, angle=angle, length=length)


sd.pause()

