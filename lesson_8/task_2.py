"""
2. Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и
False иначе.

"""


def is_year_leap(year_now):
    if not year_now % 400:
        return True
    if not year_now % 4:
        if not year_now % 100:
            return False
        else:
            return True
    return False


print(is_year_leap(int(input('Укажите год: '))))
