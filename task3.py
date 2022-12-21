# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def get_random_float_list(len_list, multiplier=100):
    return [round(random.random()*multiplier, 2) for _ in range(len_list)]

def difference_max_min_float(i_list):
    float_list = [i % 1 for i in i_list]
    return round(max(float_list) - min(float_list), 2)


new_list = get_random_float_list(5)
print(new_list)
dif = difference_max_min_float(new_list)
print(dif)
