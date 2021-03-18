def draw_filled_rectangle(field, todo):
    x, y = todo[1], todo[2]
    w, h = todo[3], todo[4]
    char = todo[-1]
    background = field[-1]
    x_map, y_map = field[0], field[1]

    mas = [[background for x in range(x_map)] for y in range(y_map)]
    for y1 in range(h + y):
        for x1 in range(w + x):
            if h + y >= y1 >= y and w + x >= x1 >= x:
                mas[y1][x1] = char
    return mas
