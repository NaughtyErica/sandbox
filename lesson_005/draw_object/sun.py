import simple_draw as sd


def draw_sun(center=sd.get_point(500, 500), radius=30, length_ray=100, color=sd.COLOR_YELLOW):
    sd.circle(center_position=center, radius=radius, width=0, color=color)
    for i in range(0, 360, 30):
        sun_ray = sd.get_vector(start_point=center, angle=i, length=length_ray, width=4)
        sun_ray.draw(color=color)
    sd.circle(center_position=center, radius=radius + 15, width=15, color=sd.background_color)
