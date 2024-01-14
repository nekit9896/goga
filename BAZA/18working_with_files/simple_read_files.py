file = open("text.txt", "r")
# print(file.read())  # вывести весь файл
# print(file.read(4))  # вывести первые 4 символа

# считывать файл построчно:
for i in file:
    print(i)
    # print(i, end='')  # добавляем в конец пустую строку, чтобы выводить результат

file.close()
