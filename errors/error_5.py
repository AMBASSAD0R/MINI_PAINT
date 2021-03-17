from errors.error_6 import error_6
from additional_function import ft_split


def error_5(path):
    with open(path) as file:
        data = []
        for i in ft_split(file.read(), '\n'):
            data.append(i)
        data_0 = data[0]
        data_1 = data[1]
    for i in data_0:
        try:
            int(i)
        except:
            print('ValueError: 1 string value was expected but 2 were given')
            return False
    for i in data_1:
        try:
            int(i)
        except:
            print('ValueError: 1 string value was expected but 2 were given')
            return False
    return error_6(path)
