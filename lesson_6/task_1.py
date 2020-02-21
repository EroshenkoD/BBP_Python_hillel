"""
При помощи вложенных циклов (можно while, можно for) нарисовать следующие фигуры
представленные ниже. Пользователь вводит, с клавиатуры, высоту фигуры в символах.

"""

h = int(input('Введите высоту фигуры: '))

# Выводит полый треугольник
for i in range(h):
    if i == h - 1:
        print(' ', end='')
        for j in range((h * 2) - 1):
            print('*', end='')
    else:
        for j in range(h * 2):
            if h - i == j or j == h + i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

print('\n')

# Выводит заполненный треугольник
for i in range(h):
    for j in range((h * 2)):
        if h - i <= j <= h + i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print('\n')

# Выводит ромб
for i in range(h):
    for j in range((h * 2)):
        if h - i <= j <= h + i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
else:
    for i in range(2, h+1):
        for j in range(h * 2):
            if i == j or j == ((h * 2) - i):
                print('*', end='')
            else:
                print(' ', end='')
        print()

print('\n')

# Выводит ромб, в нижнем треугольнике с центральной линией
for i in range(h):
    for j in range((h * 2)):
        if h - i <= j <= h + i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
else:
    for i in range(2, h+1):
        for j in range(h * 2):
            if i == j or j == ((h * 2) - i) or j == h:
                print('*', end='')
            else:
                print(' ', end='')
        print()
