from errors.error_8 import *


def error_6(path):
    with open(path) as file:
        data = file.read()
        data = ft_split(data, '\n')
    if ft_len(ft_split(data[0])) == 3 and 5 <= ft_len(ft_split(data[-1])) <= 6:
        print('6: Successfully passed')
        return error_8(path)
    print(colored('Error6', 'red'))
    return False
