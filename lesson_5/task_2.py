"""
2. Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов. Используйте для решения
задачи функцию `count`
"""

s = input('Введите строку: ')

text_output = 'Дана строка: "{s}", она состоит из {col_words} слов'

print(text_output.format(s=s, col_words=s.strip().count(' ')+1))