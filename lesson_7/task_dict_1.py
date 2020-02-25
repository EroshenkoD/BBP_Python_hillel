"""
1. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте,
сколько раз оно встречалось в этом тексте.
Задачу необходимо решить с использованием словаря.

"""

out_text = 'Слово "{}" встречается: {} раз.'

text = input('Введите строку-текст: ')

exception_symbol = [',', '.']

for symbol in exception_symbol:
    text = text.replace(symbol, '')

list_word = text.lower().strip().split(' ')

d = {}

for word in list_word:
    if word in d:
        continue
    d[word] = list_word.count(word)
    print(out_text.format(word, d[word]))



