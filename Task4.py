# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
from itertools import repeat
with open("input.txt", "r") as file:
    str1 =  file.read()
def coding(str):
    code = []
    count = 1
    for i in range(len(str)-1):
        if i <= len(str):
            if str[i] == str[i + 1]:
                count += 1
            else:
                code.append(count)
                code.append(str[i])
                count = 1
    code.append(count)
    code.append(str[-1])
    return code
def uncoding(str):
    str = list(str)
    code = []
    i =0
    while i in range(len(str)-1):
        str[i] = int(str[i])
        code.extend(repeat(str[i+1], str[i]))
        i += 2
    return code
def write_in_file (str1, func):
    with open("output.txt", "w") as file:
        file.write(("".join(map(str,func(str1)))))
uncoding(str1)                  # функция восстановления
# coding(str1)                    # функция сжатия
write_in_file(str1, uncoding)     # неоюходимо выбрать нужную функцию