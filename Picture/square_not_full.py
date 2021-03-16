def square_not_full(x, y, w, h, bg):
    """
    Пустой квадрат
    """
    mas = [[] for _ in range(h + y)]
    for yy in range(h + y):
        for xx in range(w + x):
            mas[yy].append('')  # хз надо ли это

    for yy in range(h + y):
        for xx in range(w + x):
            if (xx >= x and yy == y) or (xx == x and yy >= y) or (xx == x + w - 1 and yy >= y) or\
                    (xx >= x and yy == y + h - 1):
                mas[yy][xx] = bg
    return mas



# print(square_not_full(1,3,4, 5, '*'))
# xx = square_not_full(1, 3, 4, 5, '*')
# for x in range(len(xx)):
#     print(*xx[x])
