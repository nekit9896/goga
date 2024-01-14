word = "htucyivubinlm"
print(word[2])
# длина списка и количество одинаковых
print(len(word))
print(word.count("i"))
# повысить/понизить регистр
print(word.upper())
print(word.lower())
print(word.isupper())
print(word.islower())

abra = "stRIngs ghosT"
# повысить регистр для первого символа ип онизить для остальных
print(abra.capitalize())
# получить индекс символа в строке
print(abra.find("I"))

words = "Football, basketball, ping-pong"
# разбить строку по символу
print(words.split(", "))
# выбрать элемент из списка который был строкой
hobby = words.split(", ")
print("выбрать по  индексу:", hobby[2])

# пример как увеличить регистр для каждого элемента списка, который был строкой
for i in range(len(hobby)):  # для каждого i в диапазоне длины списка
    hobby[i] = hobby[
        i
    ].capitalize()  # тут берем именно из переменной списка индексы и для каждого индекса применяем
    # повышение первого регистра
print(hobby)

# вернуть список к строке
result = ", ".join(
    hobby
)  # сначала указываем строку, которой будем разделять внутри новой строки символы (бывшие
# элементы списка)
print(result)
