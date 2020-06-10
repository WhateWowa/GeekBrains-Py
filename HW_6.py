# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from colorama import Fore

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            if self.__color == "Red":
                print(Fore.RED + 'Red - 7 sec')
                sleep(7)
                print(Fore.YELLOW + 'Yellow - 2 sec')
                sleep(2)
                print(Fore.GREEN + 'Green - 5 sec')
                sleep(5)
                break
            else:
                if self.__color == 'Yellow':
                    print(Fore.YELLOW + 'Yellow - 2 sec')
                    sleep(2)
                    print(Fore.GREEN + 'Green - 5 sec')
                    sleep(5)
                    break
                else:
                    if self.__color == 'Green':
                        print(Fore.GREEN + 'Green - 5 sec')
                        sleep(5)
                        break
                    else:
                        print(Fore.LIGHTBLUE_EX + 'Wrong Color!')
                        break

print(Fore.LIGHTMAGENTA_EX + 'Start 1st Task')
start_color = TrafficLight('Red')
print(Fore.RESET + "Start color: ", start_color._TrafficLight__color)
start_color.running()
print(Fore.RESET + 'Stop 1st Task')

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * числом толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, width, length):
        self._length = length
        self._width = width
        self.mass = 25
        self.depth = 5

    def calculate(self):
        print('Масса асфальта:', (self._length * self._width * self.mass * self.depth) / 1000, 'тонн')

print('Start 2nd Task')
road = Road(20, 15000)
print('Длина: ', road._length, 'метров')
print('Ширина: ', road._width, 'метров')
road.calculate()
print('Stop 2nd Task')

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

dict = {
    'wage': 20000,
    'bonus': 5000
}

class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        x = dict['wage']
        y = dict['bonus']
        self.wage = int(x)
        self.bonus = int(y)
        self._income = int(x + y)
        print(' Имя: ', self.name, '\n', 'Фамилия: ', self.surname, '\n', 'Должность: ', self.position, '\n', 'ЗП: ', self.wage, '\n', 'Премия: ', self.bonus)

class Position(Worker):

    def get_full_name(self):
        print('ФИО:', self.name, self.surname)

    def get_full_income(self):
        print('Доход:', self._income)

print('Start 3rd Task')
pos1 = Position('Ivan', 'Golunov', 'Spec')
pos1.get_full_name()
pos1.get_full_income()
print('Stop 3rd Task')
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'Поехала')

    def stop(self):
        print(self.name, 'Остановилась')

    def turn(self):
        print(self.name, 'Поворот внетуда')

    def show_speed(self):
        print('Скорость:', self.speed)

class TownCar(Car):

    def Town(self):
        print('TownCar', self.name, ':', self.speed, 'км/ч')

    def show_speed(self):
        if self.speed > 40:
            print(self.name, ', Вы превысили скорость!', 'Ваша скорость: ', self.speed)
        else:
            print(self.name, 'Я не превышаю')

class SportCar(Car):

    def Sport(self):
        print(self.name, 'say: Need For Speed"', '\n', 'Моя скорость: ', self.speed)

class WorkCar(Car):

    def Work(self):
        print('WorkCar', self.name, ':', self.speed, 'км/ч')

    def show_speed(self):
        if self.speed > 60:
            print(self.name, ', Вы превысили скорость!', 'Ваша скорость: ', self.speed)
        else:
            print(self.name, 'say: Я не превышаю')

class PoliceCar(Car):

    def Police(self):
        print(self.name, self.is_police, 'say: Поймать всех нарушителей скоростного режима')

print('Start 4th Task')
workcar1 = WorkCar(70, 'Blue', 'Lada', 'Work')
workcar1.go()
workcar1.show_speed()
workcar1.turn()
workcar1.stop()
workcar2 = WorkCar(50, 'White', 'KIA', 'Work')
workcar2.go()
workcar2.Work()
workcar2.show_speed()
workcar2.stop()
towncar1 = TownCar(50, 'White', 'KIA', 'Town')
towncar1.go()
towncar1.Town()
towncar1.show_speed()
towncar1.stop()
towncar2 = TownCar(30, 'Black', 'Lada', 'Town')
towncar2.go()
towncar2.Town()
towncar2.turn()
towncar2.show_speed()
towncar2.turn()
towncar2.stop()
policcar = PoliceCar(120, 'Black-White', 'Ford', 'Police')
policcar.go()
policcar.Police()
policcar.show_speed()
sportcar = SportCar(200, 'Purple', 'Lamborgini', 'Sport')
sportcar.go()
sportcar.turn()
sportcar.Sport()
sportcar.show_speed()
print('Stop 4th Task')

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(self.title)
        print('"Запуск отрисовки."')

class Pen(Stationery):

    def draw(self):
        print(self.title)
        print('"Запуск отрисовки ручкой"')

class Pencil(Stationery):

    def draw(self):
        print(self.title)
        print('"Запуск отрисовки карандашом"')

class Handle(Stationery):

    def draw(self):
        print(self.title)
        print('"Запуск отрисовки маркером"')

print('Start 5th Task')
palka = Stationery('palka')
palka.draw()
pen = Pen('Pen')
pen.draw()
pencil = Pen('Pencil')
pencil.draw()
handle = Pen('Handle')
handle.draw()
print('Stop 5th Task')
