from termcolor import colored

import additional_function
from errors.error_5 import *


def error_4(path):
    if additional_function.ft_split(path, '.')[-1] == 'it':
        print('4: Successfully passed')
        return error_5(path)
    print(colored("Error: Operation file has not correct extension", 'red'))
    return False
