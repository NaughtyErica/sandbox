
from dis import dis


def print_path(param):
    lp = len(param)
    print(lp, param)
    return lp


dis(print_path)
