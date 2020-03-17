"""
2. Имеется строка вида: AABABBAABBBAB. Необходимо написать функцию которая заменит буквы A на B, а B, соответственно,
на A. Замену можно производить ТОЛЬКО используя функцию replace(). В результате применения функции к исходной строке,
 функция должна вернуть строку: BBABAABBAAABA
"""
s = 'AABABBAABBBAB'


def replace_A_and_B(stroka):
    return stroka.replace('A', 'b').replace('B', 'a').upper()


print(replace_A_and_B(s))
