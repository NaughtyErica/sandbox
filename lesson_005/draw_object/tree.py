import simple_draw as sd
import random as rand


def draw_branches_rand(start_point=sd.get_point(300, 30), angle=90, length=100):
    if length < 7:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle + sd.random_number(10, 15), length=length, width=1)
    v2 = sd.get_vector(start_point=start_point, angle=angle - sd.random_number(10, 15), length=length, width=1)
    if 5 <= length <= 12:
        v1.draw(color=sd.COLOR_GREEN)
        v2.draw(color=sd.COLOR_GREEN)
    else:
        v1.draw()
        v2.draw()

    next_point1 = v1.end_point
    next_point2 = v2.end_point
    next_angle1 = angle + sd.random_number(10, 15)
    next_angle2 = angle - sd.random_number(10, 15)
    random_number = rand.random()
    if random_number < 0.25:
        next_length = length * (0.72 + random_number)
    elif random_number > 0.75:
        next_length = length * (0.9 * random_number)
    else:
        next_length = length * 0.6

    draw_branches_rand(start_point=next_point1, angle=next_angle1, length=next_length)
    draw_branches_rand(start_point=next_point2, angle=next_angle2, length=next_length)


# root_point = sd.get_point(300, 30)
# draw_branches_rand(start_point=root_point, angle=90, length=120)
# ===========================================================================================


