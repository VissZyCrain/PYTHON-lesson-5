# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
os.system('cls')

print('Задача № 3')

import random

def coding(text):
    if len(text) < 1:
        return ""
    count = 0
    el = text[0]
    result = ""
    for elem in text:
        if elem == el:
            count += 1
        else:
            result += str(count) + el
            count = 1
            el = elem
    else:
        result += str(count) + el
    return result

def decoding(text):
    if len(text) < 1:
        return ""
    num = ""
    result = ""
    for elem in text:
        if elem.isdigit():
            num += elem
        else:
            for i in range(int(num)):
                result += elem
            else:
                num = ""
    return result

print("Кодирование")
print(coding("abc"))
print("Декодирование")
print(decoding("3a4b2c3b"))