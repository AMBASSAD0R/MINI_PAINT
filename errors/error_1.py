import os
from additional_function import *


def error_1(filename):
    if ft_len(ft_split(os.path.abspath(filename))) == 1:
        return True
    return False
