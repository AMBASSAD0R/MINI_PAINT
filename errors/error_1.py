from additional_function import *
from errors.error_2 import error_2


def error_1(path):
    if ft_len(ft_split(path, ' ')) == 1:
        return error_2(path)
    print('Error: a lot of arguments')
    return False
