class Cats:
    name = None  # называются поля - работает как переменные
    age = None  # называются поля - работает как переменные
    color = None  # называются поля - работает как переменные
    description = None  # называются поля - работает как переменные

    def set_data(self, name, age, color, description):
        self.name = name  # чтобы обратиться к полям из строк 2-5 прописываем self. - в своем классе находим
        self.age = age
        self.color = color
        self.description = description

    def get_data(self):
        return print(
            "Имя кота:",
            self.name,
            "\nВозраст кота:",
            self.age,
            "\nЦвет кота:",
            self.color,
            "\nОписание кота:",
            self.description,
        )


cat1 = Cats()  # создаем наследный объект
cat1.name = "Boris"
cat1.color = "black"
cat1.age = 4
cat1.description = "good"

cat2 = Cats()  # создаем еще один наследный объект
cat2.name = "Pop"
cat2.color = "white"
cat2.age = 3
cat2.description = "not good"

cat3 = Cats()
cat3.set_data("Pavel", 5, "red", "very good")

print(cat1.name)
print(cat2.name)
print(cat3.name)
cat3.get_data()
