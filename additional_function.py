def ft_len(st):
    kol = 0
    for i in st:
        kol += 1
    return kol


def ft_split(string):
    tmp = ''
    mass = []
    for ch in string:
        if ch == ' ' and tmp:
            mass.append(int(tmp))
            tmp = ''
        else:
            tmp += ch
    if tmp:
        mass.append(int(tmp))
    return mass