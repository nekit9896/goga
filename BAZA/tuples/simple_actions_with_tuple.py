data = (1, 3, "gg", 4, 54, 55.7)
# Элементы кортежа изменять нельзя
# В кортеж нельзя добавлять/удалять элементы
# Кортежи весят меньше списков
# Срезы работают в кортежах как и в строках
print(data[1])
print(data[1:6])
print(data[1:6:2])
# Посчитать количество элементов равных заданному
print(data.count(54))
# Длина кортежа
print(len(data))

# Можно создать кортеж без скобок
data1 = 1, 3, 56, "gg"
print(data1)
