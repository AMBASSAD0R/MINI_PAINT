from errors.error_6 import error_6
from additional_function import *


def error_5(path):
    with open(path) as file:
        data = []
        for i in ft_split(file.read(), '\n'):
            data.append(i)
    if ft_len(data) == 2:
        return error_6(path)
    print('Error5: 1 operation was expected')
    return False
