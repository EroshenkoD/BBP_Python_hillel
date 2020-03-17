"""
1. Необходимо написать функцию для проверки корректности пароля. Функция принимает в качестве параметра пароль который
 необходимо проверить и возвращает True если пароль верный, иначе False.
Правила которым должен соответствовать пароль:
a. длина пароля должна быть больше или равна 8 символам
b. пароль должен содержать символы латинского алфавита верхнего и нижнего регистров
(a - z и  A - Z обязательно должны присутствовать оба регистра)
c. пароль должен содержать цифры от 0 до 9 (минимум 1 символ)
d. пароль должен содержать специальные символы: @ # % & _ (минимум 1 символ)
Можно использовать функции isnumeric(), isupper(), islower().
"""
import string


def check_password(password):
    pass_have_numb = False
    pass_have_letter_up = False
    pass_have_letter_low = False
    pass_have_spec_simbol = False

    if len(password) < 9:
        return False

    list_spec_simbol = ['@', '#', '%', '&', '_']

    list_all_simbol = list_spec_simbol.copy()
    list_all_simbol += list([x for x in string.ascii_letters])
    list_all_simbol += list([str(x) for x in range(10)])

    for i in password:
        if i in list_all_simbol:

            if not pass_have_numb:
                if i.isnumeric():
                    pass_have_numb = True

            if not pass_have_letter_up:
                if i.isupper():
                    pass_have_letter_up = True

            if not pass_have_letter_low:
                if i.islower():
                    pass_have_letter_low = True

            if not pass_have_spec_simbol:
                if i in list_spec_simbol:
                    pass_have_spec_simbol = True

        else:
            return False

    if not pass_have_numb or not pass_have_letter_up or not pass_have_letter_low or not pass_have_spec_simbol:
        return False

    return True


q = input("""Укажите пароль, он должен соответсвтовать следующим требованиям:
    a. длина пароля должна быть больше или равна 8 символам
    b. пароль должен содержать символы латинского алфавита верхнего и нижнего регистров
        (a - z и  A - Z обязательно должны присутствовать оба регистра)
    c. пароль должен содержать цифры от 0 до 9 (минимум 1 символ)
    d. пароль должен содержать специальные символы: @ # % & _ (минимум 1 символ)
""")

print(check_password(q))
