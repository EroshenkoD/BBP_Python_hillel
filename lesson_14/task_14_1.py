"""
1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
 Андрей Говорухи 6 6 1 4 9 9 10 4 8 2 3 8
 Василий Петров 2 9 4 7 6 6 3 6 5 5 2 4
 Гавриил Варфаломеев 10 10 4 10 7 9 4 6 8 1 1 1
 Игнат Тюльпанов 8 1 4 1 1 5 2 5 2 2 10 8
 Илья Муромцев 1 6 4 7 10 9 5 3 7 4 7 2
 Кощей Бессмертный 3 10 1 4 1 8 10 6 2 10 7 4
 Максим Мухин 10 8 9 9 5 8 6 5 7 2 4 10
 Маргарита Мартынова 9 1 5 1 10 10 2 4 4 9 8 10
 Петр Николаев 2 9 5 9 1 2 8 7 8 1 9 1
 Полина Гусева 9 2 8 7 3 9 9 5 1 9 2 6
 Спиридов Тереньтьев 4 7 7 3 10 9 7 2 10 9 8 1
 Станислав Трердолобов 8 1 6 1 4 1 10 8 8 1 8 8
 Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести
средний балл по классу. Так же,
 записать в новый файл всех учащихся в формате "Фамилия И. Ср. балл":
 Говорухи А. 5.83
 Петров В. 4.92
 Варфаломеев Г. 5.92
 Тюльпанов И. 4.08
 Муромцев И. 5.42
 Бессмертный К. 5.5
 Мухин М. 6.92
 Мартынова М. 6.08
 Николаев П. 5.17
 Гусева Г. 5.83
 Тереньтьев С. 6.42
 Трердолобов С. 5.33
 Выравнивание колонок - желательно!

"""
dict_class = {}

with open('file.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        lst_line = line.strip().replace('\n', '').split(' ')
        key = ''
        for i in lst_line:
            if i.isalpha():
                key += i + ' '
        dict_class[key] = []
        for i in lst_line:
            if i.isdigit():
                dict_class[key].append(int(i))

mid_bal_in_class = 0
print('Средний бал ниже 5 у следующих студентов:')

with open('file_1.txt', 'w', encoding='UTF-8') as file_1:
    for key, value in dict_class.items():
        dict_class[key] = [value, round(sum(value)/len(value), 2)]
        if dict_class[key][1] < 5:
            print('{:<30}{:<5}'.format(key, dict_class[key][1]))
        mid_bal_in_class += dict_class[key][1]
        file_1.write('{:<30}{:<5}\n'.format(key, dict_class[key][1]))


print()
print('Средний бал класса: {}'.format(round(mid_bal_in_class/len(dict_class), 2)))








