#!/usr/bin/env python3

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candy_tray = BoundedSemaphore(MAX)


def refill():
    lock.acquire()
    print("Refilling candy...", end=" ")
    try:
        candy_tray.release()
    except ValueError:
        print("full, skipping")
    else:
        print("OK")
    lock.release()


def buy():
    lock.acquire()
    print("Buying candy...", end=" ")
    if candy_tray.acquire(False):
        print("OK")
    else:
        print("empty, skipping")
    lock.release()


def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))


def _main():
    print("starting at:", ctime())
    n_loops = randrange(2, 6)
    print("THE CANDY MACHINE (full with %d bars)!" % MAX)
    Thread(target=consumer, args=(randrange(n_loops, n_loops+MAX+2),)).start()  # buyer
    Thread(target=producer, args=(n_loops,)).start()  # vndr


@register
def _atexit():
    print("all done at:", ctime())


if __name__ == "__main__":
    _main()
