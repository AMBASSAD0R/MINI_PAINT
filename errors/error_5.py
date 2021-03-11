import os


def error_5(filename):
    with open(filename) as filename:
        cash = filename.read()
        cash = cash.split('\n')
        if cash[-1].count('r') + cash[-1].count('R') + cash[-1].count('L') + cash[-1].count('c') + cash[-1].count(
                'C') == 1:
            return True
        return False


print(error_5('qwe'))
