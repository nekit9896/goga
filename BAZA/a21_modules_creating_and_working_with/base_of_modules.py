"""
По сути модули - это библиотеки которые мы импортируем, среди них есть и встроенные в питон,
есть и те что мы разработали самостоятельно,
есть и такие, которые мы импортируем у сторонних разработчиков (оф сайт пакетного менеджера pip (https://pypi.org/)
пакетный менеджер pip - это просто приложение, которое автоматически встает вместе с python
"""
import time
import datetime as d  # можно сделать алиас названия библиотеки, в данном случае 'd'
import sys  # если нужно получить/использовать информацию о пользователе
import os, platform

# print(d.datetime.now())
# time.sleep(3)
print(d.datetime.now().date().weekday())

print(sys.version)  # отдает путь к текущему файлу/проекту
print(os.name)  # название операционки
print(platform.system())  # название операционки

# Импорт собственного модуля из того же репозитория
import my_own_module
from my_own_module import three_numbers

my_own_module.hi("Nikita")
print(three_numbers(3, 5, 7))

# Импорт собственного модуля из другого репозитория
from BAZA.a19_try_except.try_except import razdelitel

razdelitel()
