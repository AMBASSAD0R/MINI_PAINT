import os
from errors.error_6 import error_6


def error_5(filename):
    with open(filename) as filename:
        cash = filename.read()
        cash = cash.split('\n')
        if cash[-1].count('r') + cash[-1].count('R') + cash[-1].count('L') + cash[-1].count('c') + cash[-1].count(
                'C') == 1:
            return error_6(filename)
        return False
