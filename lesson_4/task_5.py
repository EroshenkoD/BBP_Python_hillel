"""
5. Программа запрашивает ввод последовательности целых чисел, пока не будет введён 0. Как только
будет введён 0 (ноль), программа должна посчитать и вывести на экран:
- количество введённых чисел (завершающий 0 не считается)
- их сумму
- среднее арифметическое (не считая завершающего числа 0)
- определить максимальное и минимальное значение
- определить количество чётных и не чётных элементов в последовательности

"""
text = """
- количество введённых чисел (завершающий 0 не считается): {col_input}
- сумма чисел: {sum_input}
- среднее арифметическое (не считая завершающего числа 0): {mid_input}
- минимальное значение: {min_value}
- максимальное значение: {max_value}
- количество чётных элементов  в последовательности: {chet_value}
- количество не чётных элементов в последовательности : {not_chet_value}
"""

col_input = 0
sum_input = 0
min_value = 0
max_value = 0
mid_input = 0
chet_value = 0
not_chet_value = 0

while True:

    n = int(input("Укажите целое число: "))

    if not n:
        print(text.format(col_input=col_input, sum_input=sum_input, min_value=min_value, max_value=max_value,
                          mid_input=mid_input, chet_value=chet_value, not_chet_value=not_chet_value))
        break

    col_input += 1

    sum_input += n

    if not min_value:
        min_value = n
    else:
        if n < min_value:
            min_value = n

    if n > max_value:
        max_value = n

    mid_input = sum_input / col_input

    if n % 2 == 0:
        chet_value += 1
    else:
        not_chet_value += 1


