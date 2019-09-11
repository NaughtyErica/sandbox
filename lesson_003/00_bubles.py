# -*- coding: utf-8 -*-

import simple_draw as sd
import random as rand
sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.Point(x=80, y=80)
for i in range(1, 4):
    r = 50 + i*5
    sd.circle(center_position=point, radius=r, color=sd.COLOR_PURPLE, width=1)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def draw_bubbles(center, rad, step, clr, width):

    for ii in range(1, 4):
        sd.circle(center_position=center, radius=rad + ii * step, color=clr, width=width)


point = sd.Point(x=230, y=80)
color = sd.COLOR_DARK_RED
draw_bubbles(point, 50, 10, color, 3)

# Нарисовать 10 пузырьков в ряд
color = sd.COLOR_DARK_ORANGE
for i in range(10):
    point = sd.Point(x=50 + i * 120, y=230)
    draw_bubbles(point, 30, 5, color, 1)


# Нарисовать три ряда по 10 пузырьков
color = sd.COLOR_YELLOW
for k in range(3):
    for i in range(10):
        point = sd.Point(x=50 + i * 120, y=350 + k*100)
        draw_bubbles(point, 30, 5, color, 1)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for i in range(100):
    x = rand.random() * 1200
    y = rand.random() * 600
    color_lst = [sd.COLOR_YELLOW,
                 sd.COLOR_PURPLE,
                 sd.COLOR_BLACK,
                 sd.COLOR_BLUE,
                 sd.COLOR_CYAN,
                 sd.COLOR_GREEN,
                 sd.COLOR_ORANGE,
                 sd.COLOR_RED,
                 sd.COLOR_WHITE,
                 sd.COLOR_DARK_ORANGE,
                 sd.COLOR_DARK_RED,
                 sd.COLOR_DARK_GREEN,
                 sd.COLOR_DARK_PURPLE,
                 sd.COLOR_DARK_BLUE,
                 sd.COLOR_DARK_CYAN,
                 sd.COLOR_DARK_YELLOW
                 ]
    color = int(rand.random() * 16)

    point = sd.Point(x, y)
    draw_bubbles(point, 25, 3, color_lst[color], 1)

sd.pause()

