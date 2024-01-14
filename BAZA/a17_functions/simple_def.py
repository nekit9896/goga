def dev_func(a, b, c):
    res = "Результат:", a + b + c
    return res


res = dev_func(4, 5, 5)  # вызываем и передаем параметр на вход
dev_func(4.5, 5.6, 5.71)
dev_func("I ", "am ", "Nikita")

print(res)
