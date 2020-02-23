"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.

"""

h = int(input('Введите высоту фигуры: '))

s_1 = '*  '
s_2 = '   '

# Выводит полый треугольник
for i in range(h):
    if i == h - 1:
        print(s_2, end='')
        for j in range((h * 2) - 1):
            print(s_1, end='')
    else:
        for j in range(h * 2):
            if h - i == j or j == h + i:
                print(s_1, end='')
            else:
                print(s_2, end='')
        print()

print('\n')

# Выводит заполненный треугольник
for i in range(h):
    for j in range((h * 2)):
        if h - i <= j <= h + i:
            print(s_1, end='')
        else:
            print(s_2, end='')
    print()

print('\n')

old_h = h
h = h // 2 + h % 2

# Выводит ромб
for i in range(h):
    for j in range((h * 2)):
        if h - i <= j <= h + i:
            print(s_1, end='')
        else:
            print(s_2, end='')
    print()
else:
    # Для того, чтоб высота фигуры была равна указаной ползователем, но в таком случаи, фигура не соответствует условию
    if not old_h % 2:
        print(s_2, end='')
        for j in range((h * 2) - 1):
            print(s_1, end='')
        print()
    #
    for i in range(2, h+1):
        for j in range(h * 2):
            if i == j or j == ((h * 2) - i):
                print(s_1, end='')
            else:
                print(s_2, end='')
        print()

print('\n')

# Выводит ромб, в нижнем треугольнике с центральной линией
for i in range(h):
    for j in range((h * 2)):
        if h - i <= j <= h + i:
            print(s_1, end='')
        else:
            print(s_2, end='')
    print()
else:
    for i in range(2, h+1):
        for j in range(h * 2):
            if i == j or j == ((h * 2) - i) or j == h:
                print(s_1, end='')
            else:
                print(s_2, end='')
        print()
