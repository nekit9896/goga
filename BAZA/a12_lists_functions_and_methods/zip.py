a = 'Алексе Иван Артем'.split()
b = 'Таня Аня Юля'.split()

for x, y in zip(a, b):
    print(f'{x} + {y}', '= \u2665')

pairs = list(zip(a, b))
print(pairs)



