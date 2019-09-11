import simple_draw as sd


def draw_smile(color=sd.COLOR_DARK_GREEN, open_eye=1):
    bot_l = sd.get_point(421, 70)
    top_r = sd.get_point(479, 120)

    left_eye = sd.get_point(437, 100)
    right_eye = sd.get_point(463, 100)

    smile_lc = sd.get_point(442, 85)
    smile_rc = sd.get_point(458, 85)

    smile_ll = sd.get_point(432, 90)
    smile_rl = sd.get_point(442, 85)

    smile_lr = sd.get_point(458, 85)
    smile_rr = sd.get_point(468, 90)

    sd.line(smile_lc, smile_rc, color=color, width=2)
    sd.line(smile_ll, smile_rl, color=color, width=2)
    sd.line(smile_lr, smile_rr, color=color, width=2)

    sd.ellipse(bot_l, top_r, color=color, width=3)
    sd.circle(left_eye, radius=6, width=1, color=color)

    if open_eye == 1:
        sd.circle(right_eye, radius=6, width=0, color=sd.COLOR_YELLOW)
        sd.circle(right_eye, radius=6, width=open_eye, color=color)
    else:
        sd.circle(right_eye, radius=6, width=open_eye, color=color)
