from termcolor import colored

from errors.error_6 import error_6
from additional_function import *


def error_5(path):
    with open(path) as file:
        data = []
        for i in ft_split(file.read(), '\n'):
            data.append(i)
    if ft_len(data) == 2:
        print('5: Successfully passed')
        return error_6(path)
    print(colored('Error5: 1 operation was expected', 'red'))
    return False
