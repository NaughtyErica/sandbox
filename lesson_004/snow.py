
import simple_draw as sd
import lesson_005.draw_object.clouds as cl
import lesson_005.draw_object.sun as s

def draw_snow():
    N = 20
    center_snowflake = []
    length_beam = []
    drift = 0
    step_snow_fall = 0
    for i in range(N):
        coord_xy = []
        x = sd.random_number(-22, 278)
        y = sd.random_number(640, 1400)
        coord_xy.append(x)
        coord_xy.append(y)
        center_snowflake.append(coord_xy)
        length_beam.append(sd.random_number(15, 20))

    while True:
        sd.start_drawing()

        for i in range(N):
            if (-20 <= center_snowflake[i][0] <= 300) and drift < center_snowflake[i][1] < 640:
                point = sd.get_point(center_snowflake[i][0], center_snowflake[i][1])
                sd.snowflake(center=point, length=length_beam[i], color=sd.background_color)
                center_snowflake[i][0] += sd.random_number(-2, 2)
                if center_snowflake[i][0] > 280:
                    center_snowflake[i][0] = 280
                center_snowflake[i][1] -= sd.random_number(2, 5)
                point = sd.get_point(center_snowflake[i][0], center_snowflake[i][1])
                sd.snowflake(center=point, length=length_beam[i])
            else:
                if drift < 20:
                    center_snowflake[i][1] -= sd.random_number(2, 5)
            if center_snowflake[i][1] < drift < 20:
                x = sd.random_number(-22, 278)
                y = sd.random_number(640, 1200)
                center_snowflake[i][0] = x
                center_snowflake[i][1] = y
                length_beam[i] = sd.random_number(15, 25)
        cl.draw_clouds()
        # sd.finish_drawing()
        # sd.sleep(0.02)
        s.draw_sun(center=sd.get_point(700 - step_snow_fall // 2, 300 + step_snow_fall // 2), length_ray=50 + drift * 2, color=sd.background_color)

        step_snow_fall += 1

        if step_snow_fall % 60 == 0:
            drift += 1

        s.draw_sun(center=sd.get_point(700 - step_snow_fall // 2, 300 + step_snow_fall // 2), length_ray=50 + drift * 2, color=sd.COLOR_YELLOW)

        sd.finish_drawing()
        sd.sleep(0.02)

        if sd.user_want_exit() or drift > 40:
            break




