def error_3(path):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            cash = file.read()
            return True
    except:
        print(f'Error: Operation file corrupted \n')
    file.close()
