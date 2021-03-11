from errors.error_4 import *

def error_3(path):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            cash = file.read()
            return error_4(path)
    except:
        print(f'Error: Operation file corrupted \n')
    file.close()
