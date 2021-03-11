import os

from additional_function import *

path = os.path.abspath('operation.it')


def error_1(path):
    if ft_len(ft_split(path, '.')[1]) == 1:
        return True
    return False
