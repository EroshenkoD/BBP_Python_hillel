"""
3. Реверс списка
  - Принцип алгоритма заключается в следующем: мы меняем местами 0-ый элемент с последним, 1-ый с предпоследним и д.т.
  - Итого количество таких обменов будет равно половине длины списка. Иначе элементы поменяются местами по-второму кругу
и вернутся в первоначальное положение.

"""
input_text = input('Укажите целое число: ')

input_list = list(input_text)

for i in range(len(input_list)//2):
    input_list[i], input_list[-1-i] = input_list[-1-i], input_list[i]

print(input_list)
