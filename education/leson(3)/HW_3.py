# 1
def my_func_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'

def my_func_1_use():
    print(my_func_1((int(input('Введите первое число: '))), (int(input('Введите второе число: ')))))


# 2
def my_func_2(**kwargs):
    return list(kwargs.values())

def my_func_2_use():
    print(my_func_2(name=input('Введите имя: '),
                s_name=input('Введите фамилию: '),
                b_date=input('Введите дату рождения: '),
                l_town=input('Введиет город проживания: '),
                email=input('Введите email: '),
                tel=input('Введите номер телефона: ')))

# 3
def my_func_3(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)

def my_func_3_use():
    print(my_func_3(4, 1, 9))

# 4
def my_func_4(x, y):
    return 1 / x ** abs(y)

def my_func_4_use():
    print(my_func_4(2, -2))

def my_func_4_1(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x

def my_func_4_1_use():
    print(my_func_4(2, -2))

# 5
def my_func_5():
    res = 0
    while True:
        numbers = input('Ввежите строку чисел или * для выход: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма {res}. Выход')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите число или *')
        print(f'Сумма {res}')

# 6
def my_func_6(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)

def my_func_6_use():
    print(my_func_6(input('Введите текст: ').split()))