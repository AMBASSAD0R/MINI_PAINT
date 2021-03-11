from additional_function import *


def error_8(filename):
    with open(filename) as filename:
        cash = filename.read()
        cash = cash.split('\n')
    length_1 = ft_len(cash[0])
    length_2 = ft_len(cash[-1])
    count_spaces_1 = 0
    count_spaces_2 = 0
    for char in cash[0]:
        if char == ' ':
            count_spaces_1 += 1
    for char in cash[-1]:
        if char == ' ':
            count_spaces_2 += 1
    if length_1 + length_2 == count_spaces_1 + count_spaces_2 - 2:
        print("Оно работает")
        return True
    else:
        print("Fuck")
        return
