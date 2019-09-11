import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def draw_rainbow(center_point=sd.get_point(500, -50), radius=500, width=20):
    step = 0
    for color in rainbow_colors:
        step += 20
        sd.circle(center_position=center_point, radius=radius + step, width=width, color=color)

