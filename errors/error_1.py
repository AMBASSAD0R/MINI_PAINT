from additional_function import *
from errors.error_2 import *


def error_1(path, file_name):
    if ft_len(ft_split(ft_split(path, '.')[1])) <= 2:
        return error_2(file_name)
    return False

print(error_1())