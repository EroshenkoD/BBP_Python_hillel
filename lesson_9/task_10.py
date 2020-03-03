"""
10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
направление сдвига (по умолчанию влево (False)).

"""

int_numb = int(input('Укажите целое число: '))
col_runk = int(input('Укажите количество разрядов сдвига: '))
derect = input('Укажите направление сдвига "влево" или "вправо": ')


def shift(numb, runk=1, der=False):

    if der:
        for _ in range(runk):
            numb = int(str(numb)[-1] + str(numb)[:-1])
    else:
        for _ in range(runk):
            numb = int(str(numb)[1:] + str(numb)[0])
    return numb


if derect == 'влево':
    if not col_runk:
        print(shift(int_numb))
    else:
        print(shift(int_numb, col_runk))
elif derect == 'вправо':
    if not col_runk:
        print(shift(int_numb, der=True))
    else:
        print(shift(int_numb, col_runk, der=True))
else:
    print('Не правильно указано направление сдвига')


