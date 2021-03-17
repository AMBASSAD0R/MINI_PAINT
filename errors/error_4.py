import additional_function
from errors.error_5 import *


def error_4(path):
    if additional_function.ft_split(path, '.')[-1] == 'it':
        return error_5(path)
    print("Error: Operation file has not correct extension")
    return False
