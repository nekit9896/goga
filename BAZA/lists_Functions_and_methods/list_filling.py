nums = [5, 2, 7, "50", False]

# вывести циклом весь список
# for i in nums:
#     print(i)
# for i in nums:
#     i *= 2
#     print(i)

# создание списка пользователем
n = int(input("Введите длину списка: "))

user_list = []
for i in range(n):  # через range(n) задали диапазон в котором будет срабатывать список
    string = "Введите " + str(i + 1) + " элемент списка: "
    user_list.append(input(string))

print(user_list)
