
def coroutine(func):
    def inner(*arg, **kwarg):
        g = func(*arg, **kwarg)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'Ready for accept message'
    message = yield x
    print('Subgen recived:', message)


class MyException(Exception):
    pass


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Down')
            break
        except MyException:
            print('My message and any execution code')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
        return average


# g = average()
# g.send(5)
# g.send(10)
# g.send(15)
#
# try:
#     g.throw(StopIteration)
# except StopIteration as exp:
#     print('Average', exp.value)

