"""1. Вводятся названия городов в строку через пробел. Необходимо сформировать список с помощью list comprehension,
содержащий названия длиной более пяти символов. Результат вывести в строчку через пробел. """


def execute_list_comp():
    arr = []
    # string = input('some city: ').split()
    string = 'Reifnitz Venezia Bled LA'.split("R")
    print(f'исходные города: {string}')
    for city in string:
        if len(city) >= 5:
            print(f'более 5ти символов в : {city}')
            arr.append(city)
        if len(city) <= 5:
            print(f'менее 5ти символов в : {city}')
    list_comp = [city for city in arr]
    print(*list_comp)
    print(type(list_comp))


execute_list_comp()


"""2. Вводится список городов в одну строчку через пробел. Необходимо создать итератор для этого списка и с помощью итератора:
  1)вывести на экран в столбик первые два значения (названия городов),
    2) при StopIteration должно появиться сообщение 'Самые лучшие студенты учат Python у Алексея'"""


# def init_iterator(n):
#     string = 'Reifnitz Venezia Bled LA'.split()
#     print(f'исходные города: {string}')
#     iterater = iter(string[:n])
#     try:
#         while True:
#             print(next(iterater))
#             # print(next(iterater))
#     except StopIteration:
#         print('stopiteration - "Самые лучшие студенты учат Python у Алексея"')
#
#
# init_iterator(2)

"""3. Определите функцию-генератор, которая бы возвращала простые числа. 
(Простое число - это натуральное число, которое делится только на себя и на 1). 
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел."""


# def get_simple_num():
#     for num in range(1, 20):
#         if num % 1 == 0:
#             print(num)
#
#
#
# simple = get_simple_num()


"""Вводится натуральное число n (n > 8). Необходимо определить функцию-генератор, которая бы выдавала пароль длиной n символов из случайных букв, цифр и некоторых других знаков.
Для получения последовательности допустимых символов для генерации паролей в программе импортированы две строки: ascii_lowercase, ascii_uppercase, на основе которых формируется общий список:
from string import ascii_lowercase, ascii_uppercase chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
Функция-генератор должна при каждом вызове возвращать новый пароль из случайно выбранных символов chars длиной n
и делать это бесконечно, то есть, вызывать ее можно бесконечное число раз. Сгенерировать случайный индекс index в диапазоне [a; b] для символа можно с помощью функции randint модуля random:
import random
random.seed(1)
index = random.randint(a, b)
Сгенерируйте с помощью этой функции первые пять паролей и выведите их в столбик (каждый с новой строки)."""

