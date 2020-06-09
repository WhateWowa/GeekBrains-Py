# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from tkinter import *

class TrafficLights:

    def __init__(self):

        window = Tk()
        window.title("Traffic Light")

        frame = Frame(window)
        frame.pack()

        self.color = StringVar()

        radio_red = Radiobutton(frame, text="Red", bg="red", variable=self.color, value="R", command=self.on_RadioChange)
        radio_red.grid(row=10, column=1)

        radio_yellow = Radiobutton(frame, text="Yellow", bg="yellow", variable=self.color, value="Y", command=self.on_RadioChange)
        radio_yellow.grid(row = 10, column = 2)

        radio_green = Radiobutton(frame, text="Green", bg="green", variable=self.color, value="G", command=self.on_RadioChange)
        radio_green.grid(row = 10, column = 3)

        self.canvas = Canvas(window, width=450, height=300, bg="white")
        self.canvas.pack()

        self.oval_red = self.canvas.create_oval(10, 10, 110, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(120, 10, 220, 110, fill="white")
        self.oval_green = self.canvas.create_oval(230, 10, 330, 110, fill="white")

        self.color.set(R)
        self.canvas.itemconfig(self.oval_red, fill="red")

        window.mainloop()

    def on_RadioChange(self):
        color = self.color.get()

        if color == R:
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == Y:
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == G:
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")

TrafficLights()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т



# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).



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