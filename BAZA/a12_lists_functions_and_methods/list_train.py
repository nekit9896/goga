a = list(range(10))
b = a  # b копирует ссылку на объект
print(
    "Имена a и b = это", "один и тот же объект" if a is b else "разные объекты"
)  # Объекты могут быть равны друг друг
# print(*a, sep='\n')
# print(sep='\n')
# b[2] = 100
# print(*a, sep='\n')

a = [1, 4, 5, 6]
b = a
print(a)
for i in range(len(a)):
    a[i] = a[i] * 10
print(a)
print(b is a)

the_list_of_the_lists = [[1, 2, 3, 4, 5], [5, 6, 7], [8, 9, 0]]
print(the_list_of_the_lists)
for the_list in the_list_of_the_lists:
    print(*the_list, sep="\t")
print(the_list_of_the_lists)

# Сгенерировать список списков
n = 1
for i in range(3):
    for k in range(3):
        the_list_of_the_lists[i][k] = n
        n += 1
    print(the_list_of_the_lists)
