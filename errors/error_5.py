import os


def error_5(filename):
    with open(filename) as filename:
        cash = filename.read()
        cash = cash.split('\n')
        if cash[-1].count('r') or cash[-1].count('R') or cash[-1].count('L') or cash[-1].count('c') or cash[-1].count(
            'C'):
            return True
        return False

