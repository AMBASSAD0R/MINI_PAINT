from additional_function import *
from errors.error_8 import *


def error_6(filename):
    with open(filename) as filename:
        cash = filename.read()
        cash = ft_split(cash, '\n')
    if ft_len(ft_split(cash[0])) == 3 and ft_len(ft_split(cash[-1])) <= 6:
        return error_8(filename)
    else:
        print(6)
        return False

