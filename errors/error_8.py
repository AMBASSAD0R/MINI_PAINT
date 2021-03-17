from additional_function import *


def error_8(path):
    with open(path) as file:
        data = []
        for i in ft_split(file.read(), '\n'):
            data.append(i)
    count_spaces = 0
    for i in data[0]:
        if i == ' ':
            count_spaces += 1
    for i in data[1]:
        if i == ' ':
            count_spaces += 1

    data_0 = ft_split(data[0])
    data_1 = ft_split(data[1])

    count_elements = ft_len(data_0) + ft_len(data_1)
    if count_elements - count_spaces == 2:
        return True
    print('Error8')
    return False
