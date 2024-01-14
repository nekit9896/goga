def summator():
    i = 0
    while i == 0:
        try:
            x = int(input("Введите число: "))
            x += 5
            i += 1
            print(x)
        except ValueError:  # тип ошибки можно отследить в логе ошибки конечно же
            print("Значение должно быть числом")


# summator()


def razdelitel():
    i = 0
    while i == 0:
        try:
            x = int(input("Введите делимое число: "))
            y = int(input("Введите делитель: "))
            z = x / y
            i += 1
            print(z)
        except ValueError:  # тип ошибки можно отследить в логе ошибки конечно же
            print("Значение должно быть числом")
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        except OverflowError:
            print("Введите число поменьше")
        except TypeError:  # Ошибки при которой нельзя
            print("Операция не может быть выполнена")
        else:  # пригодится если не сработали except'ы
            print("сработал else")
        finally:  # этот блок срабатывает вне зависимости от того выполнился ли код в любом из предыдущих блоков
            print("Сработал блок finally")


razdelitel()
