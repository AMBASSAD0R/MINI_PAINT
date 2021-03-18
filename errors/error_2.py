import os.path

from termcolor import colored

from errors.error_3 import *


def error_2(path):
    if not os.path.isfile(path):
        print(colored("Error: name file\n", 'red'))
        return False
    print('2: Successfully passed')
    return error_3(path)
