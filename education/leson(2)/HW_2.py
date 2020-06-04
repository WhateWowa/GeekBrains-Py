# 1
list1 = ['12', 12, [12], 12.0, True]
for i in list1:
    print(type(i))

# 2
list2 = list(input('Введие текст'))
for i in range(1, len(list2), 2):
    list2[i - 1], list2[i] - list2[i], list2[i - 1]
print(list2)

# 3
month = int(input('Введите месяц: '))
if month <= 0 or month >= 13:
    print('Неверный месяц')

elif 3 <= month <= 5:
    print('Весна')

elif 6 <= month <= 8:
    print('Лето')

elif 9 <= month <= 11:
    print('Осень')

else:
    print('Зима')

# 4
line = input()
words = line.split()
for i, word in enumerate(words):
    print(i, word[:10])

# 5
list5 =[7, 5, 3, 3, 2]
request = int(input('Введите  значение: '))
for index, number in enumerate(list5):
    if int(request) <= int(list5[index]):
        continue
    list5.insert(index, request)
    print(list5)
    break
else:
    list5.append(request)
    print(list5)

# 6
goods = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
analitics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input('{}: '.format(f))
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
    goods.append((num, features)) #используем кортеж
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)