#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import *

if __name__ == '__main__':
    # Создаем пустой список для хранения словарей
    trains = []

    # Ввод данных с клавы
    n = int(input("Введите количество поездов: "))
    for i in range(n):
        destination = input("Введите название пункта назначения: ")
        train_number = input("Введите номер поезда: ")
        departure_time = input("Введите время отправления: ")
        train = {
            "destination": destination,
            "train_number": train_number,
            "departure_time": departure_time
        }
        trains.append(train)

    # Сортировка списка по времени отправления поезда
    trains.sort(key=lambda x: x["departure_time"])

    # Вывод информации о поездах, направляющихся в указанный пункт назначения
    destination_input = input("Введите название пункта назначения: ")
    destination_trains = [train for train in trains if train["destination"] == destination_input]
    if destination_trains:
        for train in destination_trains:
            print(train)
    else:
        print("Поездов в указанный пункт назначения нет!", file=stderr)
