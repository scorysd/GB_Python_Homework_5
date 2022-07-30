# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
str1 = 'wyyyyyyee4egggg555feeuuuhhkjhkuuu'
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
    return code
def write_in_file (str1):
    with open("coding.txt", "w") as file:
        file.write((" ".join(map(str,coding(str1)))))
write_in_file(str1)
print(coding(str1))