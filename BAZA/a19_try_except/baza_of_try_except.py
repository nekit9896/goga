try:
    x = int(input("Введите число: "))
    x += 5
    print(x)
except ValueError:
    print("Значение должно быть числом")
