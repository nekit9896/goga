def string_def():
    string_value = input("Введите строку: ")
    try:
        str(string_value)
        return print("Все верно, вы ввели строку!")
    except:
        print("Попробуйте еще раз")
        return string_def()


def int_def():
    try:
        int_value = input("Введите целое число: ")
        int(int_value)
        return print("Все верно, вы ввели целое число!")
    except:
        print("Попробуйте еще раз")
        return int_def()


def float_def(): ######
    try:
        input(float("Введите дробное число: "))
        return print("Все верно, вы ввели дробное число!")
    except:
        print("Попробуйте еще раз")
        return float_def()


def bool_def():  ##########
    try:
        input(bool("Введите дробное число: "))
        return print("Все верно, вы ввели булево!")
    except:
        print("Попробуйте еще раз")
        return bool_def()


def list_def():
    list_value = input("Введите список: ")
    try:
        list(list_value)
        return print("Все верно, вы ввели список!")
    except:
        print("Попробуйте еще раз")
        return list_def()


def dict_def():
    dict_value = input("Введите словарь: ")
    try:
        dict(dict_value)
        return print("Все верно, вы ввели словарь!")
    except:
        print("Попробуйте еще раз")
        return dict_def()


def set_def():
    set_value = input("Введите множество: ")
    try:
        set(set_value)
        return print("Все верно, вы ввели множество!")
    except:
        print("Попробуйте еще раз")
        return set_def()


def tuple_def():
    tuple_value = input("Введите кортеж: ")
    try:
        tuple(tuple_value)
        return print("Все верно, вы ввели кортеж!")
    except:
        print("Попробуйте еще раз")
        return tuple_def()


string_def = string_def()
int_def = int_def()
float_def = float_def()
bool_def = bool_def()
list_def = list_def()
dict_def = dict_def()
set_def = set_def()
tuple_def = tuple_def()


def main():
    try:
        string_input = input("Введите строку: ")
        integer_input = int(input("Введите целое число: "))
        float_input = float(input("Введите дробное число: "))
        boolean_input = input("Введите булево значение (True/False): ").lower()
        if boolean_input == "true":
            boolean_input = True
        elif boolean_input == "false":
            boolean_input = False
        else:
            raise ValueError("Некорректное булево значение")
        list_input = eval(input("Введите список в квадратных скобках, например [1, 2, 3]: "))
        dictionary_input = eval(input("Введите словарь в фигурных скобках, например {'a': 1, 'b': 2}: "))

        print("Ваш ввод:")
        print("Строка:", string_input)
        print("Целое число:", integer_input)
        print("Дробное число:", float_input)
        print("Булево значение:", boolean_input)
        print("Список:", list_input)
        print("Словарь:", dictionary_input)
    except ValueError as ve:
        print("Ошибка:", ve)


if __name__ == "__main__":
    main()

