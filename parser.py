from additional_function import *


def parser(path):
    with open(path) as file:
        data = file.read()
        data = ft_split(data, '\n')
        data[0] = ft_split(data[0], ' ')
        data[1] = ft_split(data[1], ' ')

    field = [int(data[0][0]), int(data[0][1]), data[0][2]]

    todo = []
    command = data[1][0]
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
