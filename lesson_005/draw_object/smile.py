import simple_draw as sd


def draw_smile(color=sd.COLOR_DARK_GREEN, open_eye=1):
    bottom_left = sd.get_point(421, 70)
    top_right = sd.get_point(479, 120)

    left_eye = sd.get_point(437, 100)
    right_eye = sd.get_point(463, 100)

    smile_left_corner_center = sd.get_point(442, 85)
    smile_right_corner_center = sd.get_point(458, 85)

    smile_left_corner_left_part = sd.get_point(432, 90)
    smile_right_corner_left_part = sd.get_point(442, 85)

    smile_left_corner_right_part = sd.get_point(458, 85)
    smile_right_corner_right_part = sd.get_point(468, 90)

    sd.line(smile_left_corner_center, smile_right_corner_center, color=color, width=2)
    sd.line(smile_left_corner_left_part, smile_right_corner_left_part, color=color, width=2)
    sd.line(smile_left_corner_right_part, smile_right_corner_right_part, color=color, width=2)

    sd.ellipse(bottom_left, top_right, color=color, width=3)
    sd.circle(left_eye, radius=6, width=1, color=color)

    if open_eye == 1:
        sd.circle(right_eye, radius=6, width=0, color=sd.COLOR_YELLOW)
        sd.circle(right_eye, radius=6, width=open_eye, color=color)
    else:
        sd.circle(right_eye, radius=6, width=open_eye, color=color)
