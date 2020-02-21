"""
3. Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s`
всех символов `ch`.Для решения можно использовать только функцию `find`(rfind), операторы  if и while.

"""
text_output = 'В строке "{s}", символ "{sm}", встречается с индексом: {count}'

st = input('Введите строку: ')
sm = input('Введите один символ: ')


i = 0
count = ''

while True:

    i = st.find(sm, i)
    if i == -1:
        count = count[:-2] + '.'
        print(text_output.format(s=st, sm=sm, count=count))
        break
    i += 1
    count += str(i-1)+', '
