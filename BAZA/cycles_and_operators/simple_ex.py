# a = 10
# while True:  # Сперва выполняем цикл
#     a -= 1
#     if a == 0:  # Далее прописываем проверку
#         break

# for i in range(1, 6):
#     print(i)

# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "w":
#         count += 1
#
# print("Count:", count)

"""
Выведите столбец чисел от 34 до 67 с выводом только четных чисел.
"""
for i in range(34, 67):

    if i % 2 == 0:
        print(i)
