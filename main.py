from Creat_picture import create_mas
from Picture.square_full import square_full
from additional_function import *
from errors.error_1 import error_1


def parser(path):
    with open(path) as file:
        data = file.read()
        data = ft_split(data, '\n')
        data[0] = ft_split(data[0], ' ')
        data[1] = ft_split(data[1], ' ')

    field = [int(data[0][0]), int(data[0][1]), data[0][2]]

    todo = []
    command = data[1][0]
    todo.append(command)
    if command == 'L':
        todo.append(int(data[1][1]))
        todo.append(int(data[1][2]))
        todo.append(int(data[1][3]))
        todo.append(int(data[1][4]))
        todo.append(data[1][5])

    elif command == 'R' or command == 'r':
        todo.append(int(data[1][1]))
        todo.append(int(data[1][2]))
        todo.append(int(data[1][3]))
        todo.append(int(data[1][4]))
        todo.append(data[1][5])
    elif command == 'c' or command == 'C':
        todo.append(int(data[1][1]))
        todo.append(int(data[1][2]))
        todo.append(int(data[1][3]))
        todo.append(data[1][4])

    return field, todo


path = 'C:/Users/User/PycharmProjects/MINI_PAINT/operation.it'
if error_1(path):
    field, todo = parser(path)
    if todo[0] == 'R':
        x = todo[1]
        y = todo[2]
        w = todo[3]
        h = todo[4]
        bg = todo[5]
        xx = square_full(x, y, w, h, bg)
        for _ in range(len(xx)):
            print(*xx[_])
