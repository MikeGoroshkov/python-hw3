# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def get_random_list(len_list, max_element=10):
    return [random.randrange(0, max_element) for _ in range(len_list)]


def few_numbers_product(i_list):
    return [i_list[i] * i_list[len(i_list) - 1 - i] for i in range(round(len(i_list) / 2))]


new_list = get_random_list(7)
print(new_list)
fn = few_numbers_product(new_list)
print(fn)
