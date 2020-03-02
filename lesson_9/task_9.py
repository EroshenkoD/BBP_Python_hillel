"""
9. Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать
    список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import
    ascii_uppercase`), она содержит все буквы латинского алфавита.

"""
from string import ascii_uppercase

out_text_1 = 'Десятичное число "{}" в других системах счисления будет выглядеть следующим образом:'
out_text_2 = '- система счисления "{}", значение: {}'


def change_calculus_system(numb):
    res_change_calculus_system = {}
    list_symbol = list(range(10)) + list(ascii_uppercase)

    for i in range(2, 37):
        if i == 10:
            continue
        attitude = numb
        cod_numb_in_cs = ''
        while attitude:
            cod_numb_in_cs = str(list_symbol[attitude % i]) + cod_numb_in_cs
            attitude = attitude//i
        res_change_calculus_system[i] = cod_numb_in_cs

    return res_change_calculus_system


input_numb = int(input('Укажите десятичное число: '))

otv_fun = change_calculus_system(input_numb)
print(out_text_1.format(input_numb))

for key, value in otv_fun.items():
    print(out_text_2.format(key, value))
