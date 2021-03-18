import os

from Picture.draw_filled_rectangle import draw_filled_rectangle
from Picture.draw_empty_rectangle import draw_empty_rectangle
from Picture.draw_line import draw_line
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
    try:
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
    except:
        print('Error')

    return field, todo


path = os.path.abspath(input())

if error_1(path):
    field, todo = parser(path)

    if field[-1] == todo[-1]:
        while field[-1] == todo[-1]:
            print('Введите другой символ рисования')
            todo[-1] = input()

    if todo[0] == 'L':
        try:
            for i in draw_line(field, todo):
                print(*i)
        except:
            print('Error: draw_line')

    elif todo[0] == 'R':
        try:
            for i in draw_filled_rectangle(field, todo):
                print(*i)
        except:
            print('Error: draw_filled_rectangle')

    elif todo[0] == 'r':
        try:
            for i in draw_empty_rectangle(field, todo):
                print(*i)
        except:
            print('Error: draw_empty_rectangle')
