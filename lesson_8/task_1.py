"""
1. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
быть произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент +, сложить
их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть
строку "Неизвестная операция".

"""


def arithmetic(chislo_1, chislo_2, action):
    if action == '+':
        return chislo_1 + chislo_2
    elif action == '-':
        return chislo_1 - chislo_2
    elif action == '*':
        return chislo_1 * chislo_2
    elif action == '/':
        return chislo_1 / chislo_2
    else:
        return "Неизвестная операция"


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
act = input('Введите действие: ')

print(arithmetic(a, b, act))

