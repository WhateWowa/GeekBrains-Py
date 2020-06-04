# a = None
# print(type(a))

# num = 50
# print(abs(num))

# print(5 & 3) побитовое и
# 5 -> 0101
# 3 -> 0011
#    * 0001

# print(5 | 3) побитовое или
# 5 -> 0101
# 3 -> 0011
#    * 0111

# print(5 ^ 3) побитовое исключаемое или
# 5 -> 0101
# 3 -> 0011
#    * 0110

# print(6 >> 1)
# 6
# 2^1

# print(6 >> 1)
# 6
# 2^3 -> 8

# print(int('0101', 2)) 10
# print(bin('0101', 2)) двоичная
# print(oct('0101', 2)) 8
# print(hex('0101', 2)) 16

# print(float(50))
# a + ib
# print(complex(1, 2))

# str()
# geekbrains = 'Geekbrains'
# b = 'qweasda'
# print(a + b)
# start stop step
# print(a[::-2])

# print(len(a))
# print(a[4])
#c ="text@test.ru"
# print(c.split("@"))

# list = ['qwe', 'rty']
# print('_'.join(list))

# print(geekbrains.title())
# print(geekbrains.lower())
# print(geekbrains.upper())
# print(geekbrains.istitle())
# print('eeke' in geekbrains)
# print(geekbrains.count('e'))
# print(geekbrains.find('i'))

# my_list = [1, 2.0, '3']
# print(type(my_list[2]))
# start stop step
# print(my_list[2])
# my_list.append('4')
# my_list.insert(2, '22')
# my_list.reverse()
# a = my_list.pop()
# print(my_list.index(1))
# print(a)
# my_list = [1, 2.0, '3']
# print(2.0 in my_list)

# print("Dragon's mother")

# a = ['qwe']
# b = a.copy()
# b.append('kwa')
# print(b)
# с = 'rtas'
# c.lower()
# print(a == b)
# print(id(a))
# print(id(b))
# print(id(c))print(a is b)

# import copy
# z = [1, 2, 3]
# a = ['qwe', z]
# b = copy.deepcopy(a)
# b = a.copy()
# print(z is b)
# b[1].append('rty')
# print(a)

# tuple()
# a = (1, 2, 'qwe')
# print(type(a))

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)
# a.remove(2)
# print(a)

# a = [1, 2, 2, 2, 3, 4]
# print(set(a))

# a = dict({'name': 'Ivan', 'Sername': 'Ivanov', 'age': 10})
# print(type(a))
# print(a['name'])
#a['city'] = 'Moscow'
#print(a)
# print(a.get('qwer'))
# print(a['qwer'])
# a = dict()
# print(a.keys())
# print(a.values())
# print(a.items())

# print(b'text')
# print('ывпываывадл'.encode('utf-8'))
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# except ValueError:
#     print('Все исключения')

# a = dict({'name': 'Ivan', 'Sername': 'Ivanov', 'age': 10})
# for value in a.values():
#     print(value)
# a = 2
# ter = a if a > 2 else 0
# print(ter)