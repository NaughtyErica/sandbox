import simple_draw as sd
import random as rd

center_and_beams_snowflakes = []
quantity_snow_flakes = 0
lst_factor = [[0.4, 0.5, 0.6, 0.7, 0.8],
              [0.25, 0.3, 0.35, 0.4, 0.45],
              [50, 55, 60, 65, 70],
              ]
# factor_a=0.6, factor_b=0.35, factor_c=60


def create_snowflakes_pos(quantity=20, position_add=0, resolution=(1200, 600),
                          len_beam_min_max=(15, 20), factor_abc=(0.6, 0.35, 60)):
    global quantity_snow_flakes, center_and_beams_snowflakes, lst_factor
    count_create = quantity
    coord_x = (-100, resolution[0] + 100)
    coord_y = (resolution[1] + 70, resolution[1] * 2)
    if quantity != 1:
        quantity_snow_flakes = quantity
    else:
        quantity_snow_flakes += 1
    for i in range(count_create):
        coord_center_len_beam = []
        x = sd.random_number(coord_x[0], coord_x[1])
        y = sd.random_number(coord_y[0], coord_y[1])
        len_beam = sd.random_number(len_beam_min_max[0], len_beam_min_max[1])
        factor_a = rd.choice(lst_factor[0])
        factor_b = rd.choice(lst_factor[1])
        factor_c = rd.choice(lst_factor[2])
        coord_center_len_beam.append(x)
        coord_center_len_beam.append(y)
        coord_center_len_beam.append(len_beam)
        coord_center_len_beam.append(factor_a)
        coord_center_len_beam.append(factor_b)
        coord_center_len_beam.append(factor_c)
        if count_create != 1:
            center_and_beams_snowflakes.append(coord_center_len_beam)
        else:
            center_and_beams_snowflakes.insert(position_add, coord_center_len_beam)
      

def create_snowflakes(quantity=20, resolution=(1200, 600),
                      len_beam_min_max=(15, 35), factor_abc=(0.6, 0.35, 60)):

    global quantity_snow_flakes, center_and_beams_snowflakes, lst_factor
    count_create = quantity
    quantity_snow_flakes += quantity
    coord_x = (-100, resolution[0] + 100)
    coord_y = (resolution[1] + 70, resolution[1] * 2)

    for i in range(count_create):
        coord_center_len_beam = []
        x = sd.random_number(coord_x[0], coord_x[1])
        y = sd.random_number(coord_y[0], coord_y[1])
        len_beam = sd.random_number(len_beam_min_max[0], len_beam_min_max[1])
        factor_a = rd.choice(lst_factor[0])
        factor_b = rd.choice(lst_factor[1])
        factor_c = rd.choice(lst_factor[2])
        coord_center_len_beam.append(x)
        coord_center_len_beam.append(y)
        coord_center_len_beam.append(len_beam)
        coord_center_len_beam.append(factor_a)
        coord_center_len_beam.append(factor_b)
        coord_center_len_beam.append(factor_c)
        center_and_beams_snowflakes.append(coord_center_len_beam)
    print("Стало", quantity_snow_flakes)
    return quantity_snow_flakes


def draw_snow_flakes(color=sd.COLOR_YELLOW):
    """
        factor_a=0.6, factor_b=0.35, factor_c=60
        factor_a - место ответвления лучиков
        factor_b - длина лучиков
        factor_c - угол отклонения лучиков
    """
    global quantity_snow_flakes, center_and_beams_snowflakes
    for i in range(quantity_snow_flakes):
        if (-70 < center_and_beams_snowflakes[i][0] < 1270) and center_and_beams_snowflakes[i][1] < 700:
            point = sd.get_point(center_and_beams_snowflakes[i][0], center_and_beams_snowflakes[i][1])
            sd.snowflake(center=point, length=center_and_beams_snowflakes[i][2], color=color,
                         factor_a=center_and_beams_snowflakes[i][3],
                         factor_b=center_and_beams_snowflakes[i][4],
                         factor_c=center_and_beams_snowflakes[i][5])


def shift_coord_snow_flakes():
    global quantity_snow_flakes, center_and_beams_snowflakes
    for i in range(quantity_snow_flakes):
        center_and_beams_snowflakes[i][0] += sd.random_number(-10, 10)
        center_and_beams_snowflakes[i][1] -= sd.random_number(10, 20)


def del_snow_flake(number_snow_flake=0):
    global quantity_snow_flakes, center_and_beams_snowflakes
    center_and_beams_snowflakes.pop(number_snow_flake)
    quantity_snow_flakes -= 1


def thin_snow():
    global quantity_snow_flakes, center_and_beams_snowflakes
    number_snowflake_upper = []
    for i in range(quantity_snow_flakes):
        if center_and_beams_snowflakes[i][1] > 800:
            number_snowflake_upper.append(i)
    count_upper = len(number_snowflake_upper)
    quantity = count_upper // 2
    # for i in range(quantity):
    #     center_and_beams_snowflakes.pop(number_snowflake_upper[i])
    #     quantity_snow_flakes -= 1
    if count_upper > 0:
        print("Номер снежинки", number_snowflake_upper[0])
        print(center_and_beams_snowflakes.pop(number_snowflake_upper[0]))
        quantity_snow_flakes -= 1
        print("Отсалось", quantity_snow_flakes)


def list_flown_bottom():
    global quantity_snow_flakes, center_and_beams_snowflakes
    number_snowflake_bottom = []
    for i in range(quantity_snow_flakes):
        if center_and_beams_snowflakes[i][1] < 0 - 35:
            number_snowflake_bottom.append(i)
    return number_snowflake_bottom

