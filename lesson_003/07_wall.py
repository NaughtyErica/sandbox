# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


for step_ver in range(12):
    for step_hor in range(7):
        if step_ver % 2 == 0:
            offset = 50
        else:
            offset = 0
        bot_l = sd.Point(offset + step_hor * 100 - 50, 0 + step_ver * 50)
        top_r = sd.Point(offset + 50 + step_hor * 100, 50 + step_ver * 50)
        sd.rectangle(bot_l, top_r, color=sd.COLOR_DARK_RED, width=3)


sd.pause()
