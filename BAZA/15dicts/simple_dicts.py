country = {"s": "d", 5: 6, True: 12, tuple: (54, 65), "list": [5, "33"]}
# В словаре могут лежать строки, числа, кортежи, булевы и списки, но списки не могут быть ключом
# Получить из словаря значение по ключу
print(country["list"])
country = {"county": "Russia", "code": "RU", "lang": "russian", "population": 144}
print(country["lang"])

# Можно создать словарь через функцию dict
country = dict(county="Russia", code="RU")  ## Здесь ключом может быть только строка((
print(country)

# Перебор словаря циклом
for i in country:
    print(i)  ## Выводит только ключи

# Вывести все элементы словаря со значениями
print(country.items())

# Перебор словаря циклом с выводом значений происходит через переменные
for key, value in country.items():
    print(key, " - ", value)
