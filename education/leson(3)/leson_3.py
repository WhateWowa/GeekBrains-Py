# print(max(1, 2, 3))
# print(max('zzz', 'aaaa'))
# list1 = ['zz', 'aaa', 'sayfduey']
# print(max(list1, key=len))

# print(round(1.873847309, 4))

# for i, val in enumerate(['a', 'b', 'c'], start=1):
#     print(i, val)
# def say_hello(a):
#     print('Hello,', a)
#
# say_hello('Ivan')

# def average(numbers):
#     result = sum(numbers) / len(numbers)
#     return result, 'qwe'
#
# out = average([1, 2, 5, 3, 4])
# print(out)

# def qwe(a):
#     pass
#
# print(qwe(500))

# print('bla-bla')
# def my_print(text):
#     pass
#
# print('bla-bla')

# x = 1
#
# def test():
#     x = 2
#
# test()
# print(x)

# def my_func(name, val,  *args):
#     print(name, val, args)
#
# my_func('Ivan', 1, 2, 1, 1)

# def my_func(name, age, sername):
#     print(name, sername, age)
#
# my_func('Ivan', 50, 'Ivanov')
# my_func(age=50, sername='Ivanov', name='Ivan')

# def my_func(name, **kwargs):
#     print(name, kwargs)

# my_func(age=50, sername='Ivanov', name='Ivan')

# names = ["Igor", 'Ivan', 'Andrey']
# ages = [50, 15, 28, 33]
#
# print(list(zip(names, ages)))
# for name, age in zip(names,ages):
#     print(name, age)

# def my_func(x):
#     return x ** 2
# data = [-2, -1, 5, 20]
# result = []
# for i in data:
#     result.append(my_func(i))
#     print(result)
#
# result = list(map(my_func, data))
# result = list(filter(my_func, data))
# data = [-2, -1, 5, 20]
# result = list(map(lambda x: x ** 2, data))
# print(result)

# print(range(10))
# for i in range(5, 10, 2):
#     print(i)

def my_func(name, age, sername):
    """
    :param name
    :param age:
    :param sername:
    :return:
    """
print(my_func())