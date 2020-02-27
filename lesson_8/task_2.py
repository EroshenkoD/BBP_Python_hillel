"""
2. Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и
False иначе.

"""


def is_year_leap(year_now):
    return not year_now % 4


print(is_year_leap(int(input('Укажите год: '))))
