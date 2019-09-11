import simple_draw as sd

center_snowflake = []
length_beam = []
quantity_snow_flakes = 0


def create_snowflakes_pos(quantity=20, position_add=0, coord_x=(-100, sd.resolution[0] + 100),
                          coord_y=(sd.resolution[1] + 70, sd.resolution[1] * 2),
                          len_beam_min_max=(15, 35)):
    global quantity_snow_flakes, center_snowflake, length_beam
    count_create = quantity
    if quantity != 1:
        quantity_snow_flakes = quantity
    else:
        quantity_snow_flakes += 1
    for i in range(count_create):
        coord_xy = []
        x = sd.random_number(coord_x[0], coord_x[1])
        y = sd.random_number(coord_y[0], coord_y[1])
        coord_xy.append(x)
        coord_xy.append(y)
        if count_create != 1:
            center_snowflake.append(coord_xy)
        else:
            center_snowflake.insert(position_add, coord_xy)
        length_beam.append(sd.random_number(len_beam_min_max[0], len_beam_min_max[1]))


def create_snowflakes(quantity=20, coord_x=(-100, sd.resolution[0] + 100),
                          coord_y=(sd.resolution[1] + 70, sd.resolution[1] * 2),
                          len_beam_min_max=(15, 35)):

    global quantity_snow_flakes, center_snowflake, length_beam
    count_create = quantity
    quantity_snow_flakes += quantity
    for i in range(count_create):
        coord_xy = []
        x = sd.random_number(coord_x[0], coord_x[1])
        y = sd.random_number(coord_y[0], coord_y[1])
        coord_xy.append(x)
        coord_xy.append(y)
        center_snowflake.append(coord_xy)
        length_beam.append(sd.random_number(len_beam_min_max[0], len_beam_min_max[1]))

    return quantity_snow_flakes


def draw_snow_flakes(color=sd.COLOR_YELLOW):
    global quantity_snow_flakes, center_snowflake, length_beam
    for i in range(quantity_snow_flakes):
        if (-70 < center_snowflake[i][0] < 1270) and center_snowflake[i][1] < 700:
            point = sd.get_point(center_snowflake[i][0], center_snowflake[i][1])
            sd.snowflake(center=point, length=length_beam[i], color=color)


def shift_coord_snow_flakes():
    global quantity_snow_flakes, center_snowflake
    for i in range(quantity_snow_flakes):
        center_snowflake[i][0] += sd.random_number(-10, 10)
        center_snowflake[i][1] -= sd.random_number(10, 20)


def del_snow_flake(number_snow_flake=0):
    global quantity_snow_flakes, center_snowflake, length_beam
    center_snowflake.pop(number_snow_flake)
    length_beam.pop(number_snow_flake)
    quantity_snow_flakes -= 1


def list_flown_bottom():
    global quantity_snow_flakes, center_snowflake
    number_snowflake_bottom = []
    for i in range(quantity_snow_flakes):
        if center_snowflake[i][1] < 0 - 35:
            number_snowflake_bottom.append(i)
    return number_snowflake_bottom
