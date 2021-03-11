import os.path
from errors.error_3 import *


def error_2(name_file):
    if not os.path.isfile(name_file):
        print("ERROR: name file\n")
    return error_3(name_file)
