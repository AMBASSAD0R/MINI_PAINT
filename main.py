from errors.error_1 import error_1
from additional_function import *

file = input()
if error_1(file):
    with open(file, mode="r", encoding="UTF-8") as file:
        inp = file.read()
        file.close()
    inp = ft_split(inp, '\n')

mas_global = []  # здесь хранится основной массив с обрезаной картинкой

