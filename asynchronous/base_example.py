from time import sleep

queue = []


def counter():
    num = 0
    while True:
        print(num)
        num += 1
        yield


def printer():
    num = 0
    while True:
        if num % 3 == 0:
            print('Bang!')
        num += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)


if __name__ == '__main__':
    g1 = counter()
    g2 = printer()
    queue.append(g1)
    queue.append(g2)
    main()
