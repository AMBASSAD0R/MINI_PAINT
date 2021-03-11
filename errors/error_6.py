def error_6(filename):
    with open(filename) as filename:
        cash = filename.read()
        cash = cash.split('\n')
        return len(cash[0].split(' ')) == 3 and len(cash[-1].split(' ')) <= 6
