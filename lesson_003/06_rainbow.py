# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

step = 0
for color in rainbow_colors:
    step += 5
    start_point = sd.Point(x=50 + step, y=50)
    end_point = sd.Point(x=350 + step, y=450)
    sd.line(start_point, end_point, color=color, width=3)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

step = 0
for color in rainbow_colors:
    step += 20
    centre = sd.Point(x=500, y=-50)

    sd.circle(center_position=centre, radius=500 + step, width=20, color=color)


sd.pause()
