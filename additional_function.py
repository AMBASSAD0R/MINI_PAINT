def ft_len(st):
    kol = 0
    for _ in st:
        kol += 1
    return kol


def ft_split(string, wht_spl=' '):
    tmp = ''
    mass = []
    for ch in string:
        if ch == wht_spl and tmp:
            mass.append(tmp)
            tmp = ''
        else:
            tmp += ch
    if tmp:
        mass.append(tmp)
    return mass


def is_digit(string):
    try:
        string_1 = int(string)
        return True
    except:
        return False
