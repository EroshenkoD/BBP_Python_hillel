"""
3. Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""
out_text = 'Слово "{}" встречается больше всех: {} раз.'

text = input('Введите строку-текст: ')

exception_symbol = [',', '.']

for symbol in exception_symbol:
    text = text.replace(symbol, '')

list_word = text.lower().strip().split(' ')

d = {}
max_value = 0
max_key = ""

for word in list_word:
    if word in d:
        continue
    d[word] = list_word.count(word)
    if list_word.count(word) >= max_value:
        max_key = word

print(out_text.format(max_key, d[max_key]))


