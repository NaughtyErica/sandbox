# http://toly.github.io/blog/2014/03/05/advanced-design-patterns-in-python/

import time
from functools import wraps
from random import randint


def time_this(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"--------{start}------------")
        func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        print(f"--------{end}-------------")
        return func(*args, **kwargs)
    return wrapper


@time_this
def time_execute(n):
    rand_value_lst = [randint(1, n) for _ in range(20000)]
    rand_value_lst.sort()
    return n


nn = time_execute(100000)
print(nn)


# ---------------------------------------------------------
# class Decorator:
#
#     def __init__(self, f):
#         print("inside decorator.__init__()")
#         f()
#     # Prove that function definition has completed
#
#     def __call__(self):
#         print("inside decorator.__call__()")
#
#
# dec = Decorator
#
#
# @dec
# def function():
#     print("inside function()")
#
#
# print("Finished decorating function()")
#
# function()

# -----------------------------------------------------------
# def decorator(func_for_decorate):
#     def modify(*args, **kwargs):
#         variable = kwargs.pop('variable', None)
#         print(variable)
#         x, y = func_for_decorate(*args, **kwargs)
#         return x, y
#     return modify
#
#
# @decorator
# def func(a,b):
#     print(a**2, b**2)
#     return a**2, b**2
#
#
# func(a=4, b=5, variable="hi")
# func(a=4, b=5)

