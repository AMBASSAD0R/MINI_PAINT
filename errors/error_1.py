from additional_function import *


def error_1(path):
    if ft_len(ft_split(ft_split(path, '.')[1])) <= 2:
        return True
    return False
