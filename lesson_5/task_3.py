"""
3. Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s`
всех символов `ch`.Для решения можно использовать только функцию `find`(rfind), операторы  if и while.

"""
text_output = 'В строке "{s}", символ "{sm}", встречается раз: {count}.'

st = input('Введите строку: ')
sm = input('Введите один символ: ')

s = st
i = 0
count = 0

while True:
    s = s[i:]
    i = s.find(sm)
    if i == -1:
        print(text_output.format(s=st, sm=sm, count=count))
        break
    i += 1
    count += 1

