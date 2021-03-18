def draw_empty_rectangle(field, todo):
    x, y = todo[1], todo[2]
    w, h = todo[3], todo[4]
    char = todo[-1]
    background = field[-1]
    x_map, y_map = field[0], field[1]

    mas = [[background for x in range(x_map)] for y in range(y_map)]
    for y1 in range(h + y):
        for x1 in range(w + x):
            if (x1 >= x and y1 == y) or (x1 == x and y1 >= y) or (x1 == x + w - 1 and y1 >= y) or (
                    x1 >= x and y1 == y + h - 1):
                mas[y1][x1] = char
    return mas
