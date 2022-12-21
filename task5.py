# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#     Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(num):
    f = [0, 1, 1]
    for i in range(3, num+1):
        f.append(f[i-1] + f[i-2])
    return f
def neg_fibonacci(row):
    return [((-1)**(i+2))*row[i+1] for i in range(0, len(row)-1)]


number = int(input('Введите число: '))
fib = fibonacci(number)
neg = neg_fibonacci(fib)
all_fib = neg[::-1] + fib
print(all_fib)