"""
Необходимо создать матрицу (двухмерный список) М х N. M и N задаёт пользователь
с клавиатуры.
Обязательные условия:
1. матрица создаётся при помощи list comprehension. При создании, список
заполняется случайными числами (используйте генератор случайных чисел)
2. необходимо посчитать сумму значений каждой строки (функцию sum()
использовать НЕЛЬЗЯ). Сумма выводится напротив соответствующих строк
3. необходимо посчитать сумму значений каждой колонки (функцию sum()
использовать НЕЛЬЗЯ). Сумма выводится под соответствующей колонкой
4. Можно использовать ТОЛЬКО ОДИН, одномерный, дополнительный список
5. Можно использовать ТОЛЬКО ОДНУ дополнительную переменную
6. Вывод программы ДОЛЖЕН соответствовать примеру ниже (для форматирования
вывода, Вам понадобится функция format())
7. задача считается выполненной ТОЛЬКО при строгом выполнении всех условий.
Введите кол-во строк: 15
Введите кол-во колонок: 10
 13 20 46 33 16 50 34 33 16 45 306
 31 28 10 37 44 39 48 21 11 46 315
 22 20 15 47 33 15 24 45 34 23 278
 37 38 36 21 41 32 47 27 12 10 301
 16 42 19 12 42 35 30 37 29 34 296
 16 23 44 37 17 27 10 35 13 14 236
 22 43 18 32 32 23 48 14 34 33 299
 24 19 18 13 18 33 41 28 24 35 253
 45 44 39 41 27 19 32 34 25 42 348
 50 21 44 18 28 23 24 27 44 25 304
 23 42 49 15 36 10 24 42 50 48 339
 50 50 12 46 31 12 22 50 24 15 312
 45 31 29 28 27 14 14 25 30 28 271
 19 22 46 22 42 11 30 37 36 16 281
 39 46 44 20 39 19 20 12 50 34 323
452 489 469 422 473 362 448 467 432 448
"""
import random

col_x = int(input('Введите кол-во строк: '))
col_y = int(input('Введите кол-во колонок: '))

matrix = list([list([random.randint(10, 51) for _ in range(col_y)]) for _ in range(col_x)])

for row in matrix:
    sum_numb = 0
    list_all_numb = []
    for numb in row:
        sum_numb += numb
        print(' {} '.format(numb), end='')
    print('     ', sum_numb)

print()

for i in range(len(matrix[0])):
    sum_numb = 0
    for row in matrix:
        sum_numb += row[i]
    print('{} '.format(sum_numb), end='')







