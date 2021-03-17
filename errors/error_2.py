import os.path
from errors.error_3 import *


def error_2(path):
    if not os.path.isfile(path):
        print("Error: name file\n")
        return False
    return error_3(path)
