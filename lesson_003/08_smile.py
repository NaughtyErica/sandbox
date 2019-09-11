# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as rand
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


set_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW,
              sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_DARK_PURPLE,
              sd.COLOR_PURPLE, sd.COLOR_DARK_YELLOW, sd.COLOR_WHITE,
              sd.COLOR_DARK_ORANGE)

for color in set_colors:
    offset1 = rand.randrange(-250, 300, 40)
    offset2 = rand.randrange(-250, 300, 40)
    bot_l = sd.Point(200 + offset1, 200 + offset2)
    top_r = sd.Point(350 + offset1, 300 + offset2)

    left_eye = sd.Point(250 + offset1, 260 + offset2)
    right_eye = sd.Point(300 + offset1, 260 + offset2)

    smile_lc = sd.Point(260 + offset1, 225 + offset2)
    smile_rc = sd.Point(290 + offset1, 225 + offset2)

    smile_ll = sd.Point(240 + offset1, 235 + offset2)
    smile_rl = sd.Point(260 + offset1, 225 + offset2)

    smile_lr = sd.Point(290 + offset1, 225 + offset2)
    smile_rr = sd.Point(310 + offset1, 235 + offset2)

    sd.line(smile_lc, smile_rc, color=color, width=4)
    sd.line(smile_ll, smile_rl, color=color, width=4)
    sd.line(smile_lr, smile_rr, color=color, width=4)

    sd.ellipse(bot_l, top_r, color=color, width=4)
    sd.circle(left_eye, radius=6, width=1, color=color)
    sd.circle(right_eye, radius=6, width=1, color=color)


sd.pause()
