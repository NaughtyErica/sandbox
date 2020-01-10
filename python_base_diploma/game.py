# -*- coding: utf-8 -*-

# pip install -r requirements.txt
from astrobox.space_field import SpaceField
from python_base_diploma.kireev import UrikDrone


if __name__ == '__main__':
    scene = SpaceField(speed=4,
                       asteroids_count=10,
                       can_fight=True
                       )
    d = UrikDrone()
    d.my_team = [UrikDrone() for _ in range(4)]

    scene.go()
