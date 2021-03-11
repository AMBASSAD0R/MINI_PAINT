def ft_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def ft_split(string, ch):
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
