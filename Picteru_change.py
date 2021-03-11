mas_global = []


def create_mas(w, h, bg):
    global mas_global
    for x in range(h):
        mas_global.append([])
        for y in range(w):
            mas_global[x].append(bg)


create_mas(5, 3, "*")
print(mas_global)
for x in range(3):
    print(*mas_global[x])