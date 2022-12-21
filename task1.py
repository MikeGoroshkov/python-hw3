# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def get_random_list(len_list, max_element=10):
    return [random.randrange(0, max_element) for _ in range(len_list)]


def odd_index_sum(incoming_list):
    i = 1
    sum_elements = 0
    while i < len(incoming_list):
        sum_elements += incoming_list[i]
        i += 2
    return sum_elements


new_list = get_random_list(7)
print(new_list)
se = odd_index_sum(new_list)
print(se)
