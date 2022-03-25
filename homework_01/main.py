"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*N):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    sqr = []
    for i in N:
        sqr.append(int(i) ** 2)
    return(sqr)



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


def filter_numbers(num_list, arg):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if arg == ODD:
        return [n for n in num_list if n % 2 == 1]
    if arg == EVEN:
        return [n for n in num_list if n % 2 == 1]
    if arg == PRIME:
        return [n for n in num_list if is_prime(n)]
