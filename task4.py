# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#  Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import math

def to_binary(num):
    binary = ''
    while num != 0:
        binary += str(num % 2)
        num = math.floor(num/2)
    return "".join(reversed(binary))

number = int(input('Введите число: '))
bin_number = to_binary(number)
print(bin_number)
