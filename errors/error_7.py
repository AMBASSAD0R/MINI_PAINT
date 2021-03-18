from additional_function import ft_split
from errors.error_8 import error_8


def error_7(path):
    with open(path) as file:
        data = file.read()
        data = ft_split(data, '\n')
        data[0] = ft_split(data[0], ' ')
        data[1] = ft_split(data[1], ' ')

    for i in data[0]:
        try:
            if i < 0:
                print('Error7: wrong format')
                return False
        except TypeError:
            continue

    for i in data[1]:
        try:
            if i < 0:
                print('Error7: wrong format')
                return False
        except:
            pass

    error_8(path)


error_7('C:/Users/User/PycharmProjects/MINI_PAINT/operation.it')
