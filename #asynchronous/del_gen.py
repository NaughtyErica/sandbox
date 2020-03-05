
def coroutine(func):
    def inner(*arg, **kwarg):
        g = func(*arg, **kwarg)
        g.send(None)
        return g
    return inner


class MyException(Exception):
    pass


# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
        # except MyException:
        #     print('Ku')
            break
        else:
            print('............', message)
    return 'from subgen()'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except MyException as exp:
    #         g.throw(exp)
    result = yield from g
    print(result)


# def a():
#     yield from 'urik'
#
#
# g = a()
# next(g)
