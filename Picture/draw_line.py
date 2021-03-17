from additional_function import *


def draw_line(path):
    with open(path) as file:
        data = file.read()
        data = ft_split(data, '\n')

    size_x = int(data[0][0])
    size_y = int(data[0][3])

    x1, y1, x2, y2 = int(data[1][2]), int(data[1][4]), int(data[1][6]), int(data[1][8])

    char = data[1][-1]

    field = [['*' for _ in range(size_x)] for _ in range(size_y)]

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

    field[y][x] = char

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
        field[y][x] = char


def parser(path):
    with open(path) as file:
        data = file.read()
        data = ft_split(data, '\n')
        data[0] = ft_split(data[0], ' ')
        data[1] = ft_split(data[1], ' ')

    field = []
    size_x = int(data[0][0])
    size_y = int(data[0][1])
    background_char = data[0][2]


print(parser(input()))
