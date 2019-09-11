# -*- coding: utf-8 -*-

import simple_draw as sd
import lesson_006.snowfall as snow
# создать_снежинки(N)
tick = 0
count_snow_flakes = 0
sd.resolution = (1200, 600)
snow.create_snowflakes_pos(quantity=20, coord_x=(-100, 1300))
while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    snow.draw_snow_flakes(color=sd.background_color)
    #  сдвинуть_снежинки()
    snow.shift_coord_snow_flakes()
    #  нарисовать_снежинки_цветом(color)
    snow.draw_snow_flakes(color=sd.COLOR_WHITE)
    lst_bottom = snow.list_flown_bottom()
    quantity_deleted = len(lst_bottom)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    if quantity_deleted > 0:
        for i in range(quantity_deleted):
            snow.del_snow_flake(number_snow_flake=lst_bottom[i])
            # snow.create_snowflakes_pos(quantity=1, coord_x=(-100, 1300), position_add=lst_bottom[i])
            snow.create_snowflakes(quantity=1, coord_x=(-100, 1300))

    sd.finish_drawing()
    sd.sleep(0.1)
    tick += 1
#     if tick % 1000:
# # Загуститель
#         count_snow_flakes = snow.create_snowflakes(quantity=1, coord_x=(-100, 1300))

    if sd.user_want_exit() or count_snow_flakes > 200:
        break
sd.pause()
