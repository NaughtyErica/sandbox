#!/usr/bin/env python3
# Copyright © 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import collections
import random

random.seed(917)
# Not truly random for ease of regression testing


class Counter:

    def __init__(self, *names):
        self.anonymous = not bool(names)
        if self.anonymous:
            self.count = 0
        else:
            for name in names:
                if not name.isidentifier():
                    raise ValueError("names must be valid identifiers")
                setattr(self, name, 0)

    def __call__(self, event):
        if self.anonymous:
            self.count += event.count
        else:
            count = getattr(self, event.name)
            setattr(self, event.name, count + event.count)


class Event:

    def __init__(self, name, count=1):
        if not name.isidentifier():
            raise ValueError("names must be valid identifiers")
        self.name = name
        self.count = count


class Multiplexer:

    ACTIVE, DORMANT = ("ACTIVE", "DORMANT")

    def __init__(self):
        self.callbacks_for_event = collections.defaultdict(list)
        self.state = Multiplexer.ACTIVE

    @property
    def state(self):
        return (Multiplexer.ACTIVE if self.send == self.__active_send
                else Multiplexer.DORMANT)

    @state.setter
    def state(self, state):
        if state == Multiplexer.ACTIVE:
            self.connect = self.__active_connect
            self.disconnect = self.__active_disconnect
            self.send = self.__active_send
        else:
            self.connect = lambda *args: None
            self.disconnect = lambda *args: None
            self.send = lambda *args: None

    def __active_connect(self, event_name, callback):
        self.callbacks_for_event[event_name].append(callback)

    def __active_disconnect(self, event_name, callback=None):
        if callback is None:
            del self.callbacks_for_event[event_name]
        else:
            self.callbacks_for_event[event_name].remove(callback)

    def __active_send(self, event):
        for callback in self.callbacks_for_event.get(event.name, ()):
            callback(event)


def generate_random_events(count):
    vehicles = (("cars",) * 11) + (("vans",) * 3) + ("trucks",)
    for _ in range(count):
        yield Event(random.choice(vehicles), random.randint(1, 3))


def main():
    total_counter = Counter()
    car_counter = Counter("cars")
    commercial_counter = Counter("trucks", "vans")

    multiplexer = Multiplexer()
    for event_name, callback in (("cars", car_counter),
                                ("vans", commercial_counter), ("trucks", commercial_counter)):
        multiplexer.connect(event_name, callback)
        multiplexer.connect(event_name, total_counter)

    for event in generate_random_events(100):
        multiplexer.send(event)
    print(f"After 100 active events:  cars={car_counter.cars} vans={commercial_counter.vans} "
          f"trucks={commercial_counter.trucks} total={total_counter.count}")

    multiplexer.state = Multiplexer.DORMANT
    for event in generate_random_events(100):
        multiplexer.send(event)
    print(f"After 100 active events:  cars={car_counter.cars} vans={commercial_counter.vans} "
          f"trucks={commercial_counter.trucks} total={total_counter.count}")
    
    multiplexer.state = Multiplexer.ACTIVE
    for event in generate_random_events(100):
        multiplexer.send(event)
    print(f"After 100 active events:  cars={car_counter.cars} vans={commercial_counter.vans} "
          f"trucks={commercial_counter.trucks} total={total_counter.count}")
    

if __name__ == "__main__":
    main()
