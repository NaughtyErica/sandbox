import simple_draw as sd


def melts(depth=40):
    bottom_left = sd.get_point(0, 42 - depth)
    top_right = sd.get_point(298, 42)
    sd.rectangle(bottom_left, top_right, color=sd.background_color, width=0)