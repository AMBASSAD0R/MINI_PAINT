from additional_function import *
from errors.error_2 import error_2
from termcolor import colored


def error_1(path):
    if ft_len(ft_split(path, ' ')) == 1:
        print('1: Successfully passed')
        return error_2(path)
    print(colored('Error: a lot of arguments', 'red'))
    return False
