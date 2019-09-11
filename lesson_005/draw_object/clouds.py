import simple_draw as sd


clouds_list_coord = [(0, 570, 50),
                     (80, 570, 70),
                     (150, 570, 40),
                     (200, 570, 50),
                     (270, 570, 40),
                     ]


def draw_clouds():
    for coord in clouds_list_coord:
        sd.circle(center_position=sd.get_point(coord[0], coord[1]), radius=coord[2],
                  width=0, color=sd.COLOR_WHITE)
