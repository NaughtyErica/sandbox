# -*- coding: utf-8 -*-
import pygame
import simple_draw as sd

import lesson_006.snowfall as snow


count_snow_flakes = 0
resolution_screen = sd.resolution = (1200, 600)
snow.create_snowflakes(quantity=20, resolution=resolution_screen)
print("Усиление снегопада - S")
print("Уменьшение снегопада - W")
print("Ветер справа - A")
print("Ветер слева - D")
print("Клавиши нажимать дробно. Усиление +5 снежинок, уменьшение -1")
while True:
    sd.start_drawing()
    snow.draw_snow_flakes(color=sd.background_color)
    snow.shift_coord_snow_flakes()
    snow.draw_snow_flakes(color=sd.COLOR_WHITE)
    lst_bottom = snow.list_flown_bottom()
    quantity_deleted = len(lst_bottom)
    if quantity_deleted > 0:
        for i in range(quantity_deleted):
            snow.del_snow_flake(number_snow_flake=lst_bottom[i])
            snow.create_snowflakes_pos(quantity=1, position_add=lst_bottom[i], resolution=resolution_screen)
    sd.finish_drawing()
    # В таком вариант у меня устойчиво ловит команды клавиатуры, правда иногда дублирует их
    # а в предыдущем варианте почти не работало
    keyState = pygame.key.get_pressed()
    if keyState[pygame.K_s]:
        count_snow_flakes = snow.create_snowflakes(quantity=5, resolution=resolution_screen)
    if keyState[pygame.K_w]:
        snow.thin_snow()
    if keyState[pygame.K_a]:
        snow.wind(direction=-1)
    if keyState[pygame.K_d]:
        snow.wind(direction=1)
    sd.sleep(0.1)
    if sd.user_want_exit() or count_snow_flakes > 200:
        break
sd.pause()

# зачет!
