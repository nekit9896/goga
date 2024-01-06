person = {
    "user1": {
        "name": "Niki",
        "second_name": "Vald",
        "age:": 25,
        "address": ["Москва", "ул. Ленина", "д. 23"],
        "grades": {"math": 5.0, "russian": 4.3},
    },
    "user2": {},
}
# Вытащить из словаря в словаре улицу
print(person["user1"]["address"][1])
