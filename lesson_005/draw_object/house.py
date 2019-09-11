import simple_draw as sd


def draw_wall(bottom_left=sd.get_point(0, 0), top_right=sd.get_point(400, 400),
              brick_l=100, brick_h=50, color=sd.COLOR_DARK_RED):
    sd.rectangle(bottom_left, top_right, color=color, width=3)
    number_hor_steps = (top_right.x - bottom_left.x) // brick_l
    number_ver_steps = (top_right.y - bottom_left.y) // brick_h
    for step_ver in range(number_ver_steps):
        for step_hor in range(number_hor_steps):
            if step_ver % 2 != 0:
                offset = brick_l // 2
            else:
                offset = 0
            bot_l = sd.get_point(bottom_left.x + offset + step_hor * brick_l,
                                 bottom_left.y + step_ver * brick_h)
            top_r = sd.get_point(bottom_left.x + offset + brick_l + step_hor * brick_l,
                                 bottom_left.y + brick_h + step_ver * brick_h)
            if not(step_hor == number_hor_steps - 1 and step_ver % 2 != 0):
                sd.rectangle(bot_l, top_r, color=color, width=3)


def draw_roof(point_left=sd.get_point(0, 0), length=100):
    roof_ridge_x = point_left.x + length // 2
    roof_ridge_y = point_left.y + length // 3
    roof_ridge = sd.get_point(roof_ridge_x, roof_ridge_y)
    point_right = sd.get_point(point_left.x + length, point_left.y)
    sd.line(start_point=point_left, end_point=roof_ridge, color=sd.COLOR_DARK_GREEN, width=4)
    sd.line(start_point=point_right, end_point=roof_ridge, color=sd.COLOR_DARK_GREEN, width=4)


def draw_window(bottom_left=sd.get_point(0, 0),
                top_right=sd.get_point(50, 50), color=sd.COLOR_YELLOW):
    sd.rectangle(left_bottom=bottom_left, right_top=top_right, color=color, width=0)
    sd.rectangle(left_bottom=bottom_left, right_top=top_right, color=sd.COLOR_DARK_ORANGE, width=3)
    frame_bottom_x = (top_right.x - bottom_left.x) // 2 + bottom_left.x
    frame_bottom_y = bottom_left.y
    frame_bottom = sd.get_point(frame_bottom_x, frame_bottom_y)
    frame_top_x = frame_bottom_x
    frame_top_y = top_right.y
    frame_top = sd.get_point(frame_top_x, frame_top_y)
    sd.line(start_point=frame_bottom, end_point=frame_top, color=sd.COLOR_DARK_ORANGE, width=3)
    window_leaf_left_x = frame_top_x
    window_leaf_left_y = frame_top_y - (frame_top_y - frame_bottom_y) // 3
    window_leaf_left = sd.get_point(window_leaf_left_x, window_leaf_left_y)
    window_leaf_right_x = top_right.x
    window_leaf_right_y = window_leaf_left_y
    window_leaf_right = sd.get_point(window_leaf_right_x, window_leaf_right_y)
    sd.line(start_point=window_leaf_left, end_point=window_leaf_right, color=sd.COLOR_DARK_ORANGE, width=3)


def draw_house(bottom_left=sd.get_point(0, 0), top_right=sd.get_point(400, 200),
               window_length=150, window_height=100, brick_l=100, brick_h=50):
    draw_wall(bottom_left=bottom_left, top_right=top_right, brick_l=brick_l, brick_h=brick_h)
    roof_bottom_left = sd.get_point(bottom_left.x, top_right.y)
    draw_roof(point_left=roof_bottom_left, length=top_right.x - bottom_left.x)
    win_bottom_left_x = bottom_left.x + (top_right.x - bottom_left.x) // 2 - window_length // 2
    win_bottom_left_y = bottom_left.y + (top_right.y - bottom_left.y) // 2 - window_height // 2
    win_bottom_left = sd.get_point(win_bottom_left_x, win_bottom_left_y)
    win_top_right_x = win_bottom_left_x + window_length
    win_top_right_y = win_bottom_left_y + window_height
    win_top_right = sd.get_point(win_top_right_x, win_top_right_y)
    draw_window(win_bottom_left, win_top_right)
