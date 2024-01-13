country = {"country": "Russia", "code": "RU", "lang": "russian", "population": 144}
# get такой же как и country['code']
print(country.get("code"))
# очистить словарь country.clear()
print(country)
country1 = {"county": "Russia", "code": "RU", "lang": "russian", "population": 144}
# удалить элемент по ключу
country1.pop("code")
print(country1)
# удалить последний элемент словаря
country1.popitem()
print(country1)
# получить все ключи словаря
print(country.keys())
# Обновить значения словаря
country.update(country="Rus")
print(country.items())
country["country"] = "RUS"  # или так
print(country.items())
