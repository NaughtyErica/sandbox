import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 40

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

center_snowflake = []
length_beam = []
drift = 0
step_snow_fall = 0
delta_snow_storm = 0
for i in range(N):
    coord_xy = []
    x = sd.random_number(-40, 1240)
    y = sd.random_number(640, 1400)
    coord_xy.append(x)
    coord_xy.append(y)
    center_snowflake.append(coord_xy)
    length_beam.append(sd.random_number(15, 35))

while True:
    sd.start_drawing()
    for i in range(N):
        if (-70 <= center_snowflake[i][0] <= 1270) and center_snowflake[i][1] < 640:
            point = sd.get_point(center_snowflake[i][0], center_snowflake[i][1])
            sd.snowflake(center=point, length=length_beam[i], color=sd.background_color)
            center_snowflake[i][0] += sd.random_number(-2, 2) + delta_snow_storm * 7
            center_snowflake[i][1] -= sd.random_number(2, 5)
            point = sd.get_point(center_snowflake[i][0], center_snowflake[i][1])
            sd.snowflake(center=point, length=length_beam[i])
        else:
            center_snowflake[i][1] -= sd.random_number(2, 5)
        if center_snowflake[i][1] < 5 + drift:
            if delta_snow_storm == 1:
                if step_snow_fall % 2 == 0:
                    x = sd.random_number(-70, -40)
                    y = sd.random_number(drift, 700)
                else:
                    x = sd.random_number(-100, 1100)
                    y = sd.random_number(640, 680)
            elif delta_snow_storm == -1:
                if step_snow_fall % 2 == 0:
                    x = sd.random_number(1240, 1270)
                    y = sd.random_number(drift, 700)
                else:
                    x = sd.random_number(100, 1300)
                    y = sd.random_number(640, 680)
            else:
                x = sd.random_number(-40, 1240)
                y = sd.random_number(640, 1200)
            center_snowflake[i][0] = x
            center_snowflake[i][1] = y
            length_beam[i] = sd.random_number(15, 35)
    sd.finish_drawing()
    sd.sleep(0.02)
    step_snow_fall += 1
    if step_snow_fall % 40 == 0:
        drift += 1
    if step_snow_fall % 400 == 0:
        old_delta_snow_storm = delta_snow_storm
        delta_snow_storm = sd.random_number(-1, 1)
        if old_delta_snow_storm == -1 or old_delta_snow_storm == 1:
            delta_snow_storm = 0
    if sd.user_want_exit() or drift > 350:
        break

sd.pause()
# ===============Добавил метель! Очень хотелось, не смог удержаться от такого соблазна!========

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

# зачет!
