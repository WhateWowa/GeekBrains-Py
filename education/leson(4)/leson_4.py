# import my_module
#
# my_module.my_func(1, 2)
# my_module.pow(1, 2)
#
# import my_module as mm 70%
#
# mm.my_func(1, 2)
# mm.pow(1, 2)
#
# from my_module import pow, my_func 29%
#
# my_func(1, 2)
# pow(1, 2)
#
# from my_module import * 1%

# import time
#
# a = time.time()
# for i in range(100000000):
#     pass
#
# b = time.time()
# print(b - a)

# import math
# print(math.pi)
# print(math.floor(1.2))
# print(math.ceil(1.2))

# import sys
# print(sys.path)
# sys.path.insert(0, 'new path')

# from sys import argv
# print(argv[1:])
# if 'help' in argv[1:]:
#     print('Описание как работать с нашим скриптом')

# import time, math

# import os
# print(os.getcwd())
# os.mkdir('path')
# print(os.listdir)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new = [qwe for qwe in my_list if qwe % 2 == 0]
# new = {el: el ** 2 for el in range(30)}
# print(new)

# import random
# print(random.randint(1, 50))
# print(random.randrange(10, 20, 3))

# generator = (p*p for p in range(6))
#
# for i in generator:
#     print(i)

# def generator():
#     for el in (10, 20, 30):
#         yield el

# g = generator()
# for i in g:

# from functools import reduce, partial
# def my_func(num1, num2):
#     return num1 + num2
#
# print(reduce(my_func, [5, 10, 15]))

# def my_func(params1, params2):
#     return params1 ** params2
#
# new_func = partial(my_func, 2)
# print(new_func)
# print(new_func(4))
# print(new_func(5))

# from itertools import count, cycle
# for el in count(0):
#     print(el)
#     if el >10:
#         break

# c = 0
# for i in cycle(['1', '2', '3']):
#     print(i)
#     c += 1
#     if c > 10:
#         break