from errors.error_7 import error_7
from errors.error_8 import *


def error_6(path):
    with open(path) as file:
        data = file.read()
        data = ft_split(data, '\n')
    if ft_len(ft_split(data[0])) == 3 and 5 <= ft_len(ft_split(data[-1])) <= 6:
        return error_7(path)
    print('Error6')
    return False
