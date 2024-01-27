import itertools as it

for x, y, z in it.permutations("ABC"):
    print(x, y, z, sep=" ", end="\n")

print("\nПеребираем все варианты сочетаний")
for x, y, z in it.permutations("ABCDE", 3):  # Перебор 3 из 5
    print(x, y, z, sep=" ", end="\n")

print("\n")
print(
    "Перебираем все пары учеников по парам без повторений типа Bogdan+Timur и Timur+Bogdan"
)
for x, y in it.combinations(
    (
        "Pavel",
        "Masha",
        "Misha",
        "Tolya",
        "Olya",
        "Tanya",
        "Nikita",
        "Oleg",
        "Timur",
        "Bogdan",
    ),
    2,
):  # Комбинации (например дежурных) по 2 человека из 10
    print(x, y, sep=" ", end="\n")

for n, s in it.product(
    [1, 4, 5, 6, 7], "ABC"
):  # 'это декартово произведение поэтому появляются пары, и мы их печатаем
    print(n, s)
