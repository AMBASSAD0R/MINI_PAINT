def square_full(x, y, w, h, bg):
    """
    Полный квадрат
    """
    mas = [[] for _ in range(h + y)]
    for yy in range(h + y):
        for xx in range(w + x):
            if h + y >= yy >= y and w + x >= xx >= x:
                mas[yy].append(bg)
            else:
                mas[yy].append('')  # хз надо ли это
    return mas

# print(square_full(1,3,4, 5, '*'))
# xx = square_full(1,3,4, 5, '*')
#
# for x in range(len(xx)):
#     print(*xx[x])
