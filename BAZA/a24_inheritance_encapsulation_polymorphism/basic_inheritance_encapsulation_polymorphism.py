"""
У любого класса может быть класс наследник, который будет наследовать свойства и функции от класса родителя (супер-класса)
"""


class Buildings:
    year = None
    city = None

    def __init__(self, year, city):  # конструктор принимает два параметра
        self.city = city  # через self.city мы обращаемся к полю и будем устанавливать в него то значение которое мы
        self.year = year  # получаем из конструктора

    def get_info(self):
        return print("Год: ", self.year, "Город: ", self.city)


school = Buildings(2000, "Moscow")  # это объекты
administration = Buildings(1986, "Moscow")  # это объекты
university = Buildings(1999, "Moscow")  # это объекты

# print(school.get_info(), administration.get_info(), university.get_info())


# Допустим надо для школы добавить еще 2 новые функции, а для администрации еще 3 других функции, в таком случае можно
# создать дополнительный класс который будет все наследовать от класса Buildings, но иметь дополнительно еще 2 функции:
# class School(school):
#     countr = None
#     level = None
#
#     def __init__(self, countr, level):
#         super(Buildings, self).__init__(
#             year, city
#         )
#         self.countr = countr
#         self.level = level
#
#     def set_childs(self):
#         countr = int(input())
#         level = str(input())
#         return print("Количество: ", countr, "Уровень: ", level)


class Administrations(Buildings):
    sotrudniki = None
    position = None

    def __init__(
        self, sotrudniki, position, year, city
    ):  # Передача данных в класс конструктора
        super(Administrations, self).__init__(
            year, city
        )  # функция super() вызывает класс родитель
        self.sotrudniki = sotrudniki
        self.position = position


# school1 = School(2000, "Moscow")  # это объекты
administration1 = Administrations(38, "staff", 1986, "Moscow")  # это объекты
university1 = Buildings(1999, "Moscow")  # это объекты


# Теперь сделаем наследнику Administrations наследника LocalAdministrations и добавим ПОЛИМОРФИЗМ
class LocalAdministrations(Administrations):
    users = None
    permissions = None

    def __init__(self, users, permissions, sotrudniki, position, year, city):
        super().__init__(sotrudniki, position, year, city)
        self.users = users
        self.permissions = permissions

    def get_info(
        self,
    ):  # старый get_info из родителя не выведет поля наследников, поэтому переназначаем метод
        super().get_info()  # За счет полиморфизма можно взять метод из родительского класса, дополнить его новыми
        print(
            "Пользователи: ", self.users
        )  # полями наследников, новым функционал, надо просто обратиться к методу
        # родителя в наследнике и перписать его функционал


# school2 = School(2000, "Moscow")  # это объекты
administration2 = Administrations(38, "staff", 1986, "Moscow")  # это объекты
administration_local = LocalAdministrations(
    10, True, 38, "staff", 1986, "Moscow"
)  # это объекты
print(administration_local.get_info())
university2 = Buildings(1999, "Moscow")  # это объекты

# Инкапсуляция
