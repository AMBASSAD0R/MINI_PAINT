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
        todo.append(data[1][0])
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


def draw_line(field, todo):
    map = [[field[-1] for _ in range(field[0])] for _ in range(field[1])]

    x1 = todo[1]
    y1 = todo[2]
    x2 = todo[3]
    y2 = todo[4]
    char = todo[5]

    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    if dx < 0: dx = -dx
    if dy < 0: dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    map[y][x] = char

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        map[y][x] = char


field, todo = parser(input())
draw_line(field, todo)
