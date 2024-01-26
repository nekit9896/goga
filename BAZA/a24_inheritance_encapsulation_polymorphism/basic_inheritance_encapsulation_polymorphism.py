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

print(school.get_info(), administration.get_info(), university.get_info())


# Допустим надо для школы добавить еще 2 новые функции, а для администрации еще 3 других функции, в таком случае можно
# создать дополнительный класс который будет все наследовать от класса Buildings, но иметь дополнительно еще 2 функции:
class School(school):
    countr = None
    level = None

    def __init__(self, countr, level):
        self.countr = countr
        self.level = level

    def set_childs(self):
        countr = int(input())
        level = str(input())
        return print("Количество: ", countr, "Уровень: ", level)

