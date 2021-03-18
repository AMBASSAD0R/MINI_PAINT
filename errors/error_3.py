from termcolor import colored

from errors.error_4 import *


def error_3(path):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            cash = file.read()
        print('3: Successfully passed')
        return error_4(path)
    except:
        print(colored(f'Error: Operation file corrupted \n', 'red'))
        return False
