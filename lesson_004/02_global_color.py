# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def polygon(point=sd.get_point(0, 0), angle=0, length=100, corner=3, color=sd.COLOR_YELLOW):
    first_vector = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    first_vector.draw(color=color)
    next_vector = first_vector
    for i in range(corner - 1):
        if i == corner - 2:
            sd.line(start_point=next_vector.end_point, end_point=point, color=color)
        else:
            angle += int(360 / corner)
            next_vector = sd.get_vector(start_point=next_vector.end_point, angle=angle, length=length, width=1)
            next_vector.draw(color=color)


color_list = [sd.COLOR_RED,
              sd.COLOR_ORANGE,
              sd.COLOR_YELLOW,
              sd.COLOR_GREEN,
              sd.COLOR_CYAN,
              sd.COLOR_BLUE,
              sd.COLOR_PURPLE
              ]
color_name_list = ["красный",
                   "оранжевый",
                   "желтый",
                   "зеленый",
                   "бирюзовый",
                   "голубой",
                   "пурпурный",
                   ]
count_color = len(color_name_list)
while True:
    print('Возможные цвета фигур:')
    for i in range(count_color):
        print(i, ":", color_name_list[i])
    num_color = int(input('Введите желаемый цвет:'))
    if num_color not in range(count_color):
        print('Вы ввели некорректный номер!', num_color)
    else:
        start_point = sd.get_point(300, 200)
        angle = 0
        length = 150
        for corner in [3, 4, 5, 6, 7, 8]:
            polygon(point=start_point, angle=angle, length=length, corner=corner, color=color_list[num_color])
        sd.pause()
        break






