import additional_function
from errors.error_5 import *


def error_4(filename):
    if additional_function.ft_split(filename, '.')[-1] == 'it':
        return error_5(filename)
    else:
        print("ERROR: Operation file has not correct extension")
        return
