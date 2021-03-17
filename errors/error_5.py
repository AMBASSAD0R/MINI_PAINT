from errors.error_6 import error_6
from additional_function import ft_len


def error_5(path):
    with open(path) as file:
        data = file.readlines()
    for element in range(2, ft_len(data), 2):
        if data[element].isdigit():
            return False
    return error_6(path)
