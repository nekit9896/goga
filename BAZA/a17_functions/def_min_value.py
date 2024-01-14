# Найти минимальное значение в двух списках


def min_value(numbers):
    minimal = numbers[0]
    for i in numbers:
        if i < minimal:
            minimal = i

    return minimal


numbers1 = [6, 4, 3, 4, 5]
call_min_value1 = min_value(numbers1)
# print(call_min_value1)

numbers2 = [16, 24, 3, 4, 45, 2.6]
call_min_value2 = min_value(numbers2)
# print(call_min_value2)


def min_compare(a, b):
    if a > b:
        return b
    elif a == b:
        return f"Списки имеют одинаковые минимальные значения {a} = {b}"
    else:
        return a


call_min_compare = min_compare(call_min_value1, call_min_value2)
print(call_min_compare)
