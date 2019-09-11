# -*- coding: utf-8 -*-
import pygame
import simple_draw as sd
import lesson_006.snowfall as snow
# создать_снежинки(N)
tick = 0
count_snow_flakes = 0
resolution_screen = sd.resolution = (1200, 600)
snow.create_snowflakes(quantity=20, resolution=resolution_screen)
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
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:  # нажатие на крестик: выход
        #     running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                count_snow_flakes = snow.create_snowflakes(quantity=10, resolution=resolution_screen)
                print("увеличиваем")
            if event.key == pygame.K_w:
                snow.thin_snow()
                print("уменьшаем")

    sd.sleep(0.1)
    tick += 1
    # if tick % 1000:
    #     count_snow_flakes = snow.create_snowflakes(quantity=1, resolution=resolution_screen)
    if sd.user_want_exit() or count_snow_flakes > 200:
        break


sd.pause()
