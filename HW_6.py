# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# from time import sleep
# from colorama import Fore
#
# class TrafficLight:
#     def __init__(self, color):
#         self.__color = color
#         self.running()
#
#     def running(self):
#         while True:
#             if self.__color == "Red":
#                 print(Fore.RED + 'Red - 7 sec')
#                 sleep(7)
#                 print(Fore.YELLOW + 'Yellow - 2 sec')
#                 sleep(2)
#                 print(Fore.GREEN + 'Green - 5 sec')
#                 sleep(5)
#                 break
#             else:
#                 if self.__color == 'Yellow':
#                     print(Fore.YELLOW + 'Yellow - 2 sec')
#                     sleep(2)
#                     print(Fore.GREEN + 'Green - 5 sec')
#                     sleep(5)
#                     break
#                 else:
#                     if self.__color == 'Green':
#                         print(Fore.GREEN + 'Green - 5 sec')
#                         sleep(5)
#                         break
#                     else:
#                         print(Fore.LIGHTBLUE_EX + 'Wrong Color!')
#                         break
#
# start_color = TrafficLight('Blue')
# print(Fore.RESET + "Start color: ", start_color._TrafficLight__color)

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * числом толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

# class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#         self.mass = 25
#         self.depth = 5
#         self.calculate()
#
#     def calculate(self):
#         print('Масса асфальта:', (self._length * self._width * self.mass * self.depth) / 1000, 'тонн')
#
# road = Road(10, 2000)

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

dict()
income1 = {"wage": 20000, "bonus": 5000}
income2 = {"wage": 22000, "bonus": 3000}

class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict()
        print('Имя: ', self.name, '\n', 'Фамилия: ', self.surname, '\n', 'Должность: ', self.position, '\n', 'Доход: ', self._income)

class Position(Worker):

    def get_full_name(self):
        print('ФИО: ', self.name, self.surname)

    def get_full_income(self):
        print('Доход: ', )


pos1 = Position('Ivan', 'Golunov', 'Spec')


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.



# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.