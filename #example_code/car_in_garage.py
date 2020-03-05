from collections import namedtuple

Car = namedtuple('Car', ['color', 'brand'])


class Garage:
    def __init__(self):
        self._cars = [
            Car(color='brown', brand='Porsche'),
            Car(color='black', brand='BMW'),
            Car(color='silver', brand='Mercedes'),
            Car(color='white', brand='Lada-kalina'),

        ]

    def __len__(self):
        return len(self._cars)

    def __getitem__(self, item):
        return self._cars[item]


gar = Garage()

print(len(gar))

print(gar[0:2])

for car in gar:
    print(car.brand, car.color)
