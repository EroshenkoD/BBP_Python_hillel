"""
11. Дана строка. Замените в этой строке все появления буквы `h` на букву `H`, кроме первого и последнего вхождения.

"""
text_output = """
Дана строка: "{s}"
Строка получилась: "{start}{mid}{end}"
"""
s = input('Введите строку, в ней будут заменены все буквы "h" на "H": ')

print(text_output.format(s=s,
                         start=s[:(s.find("h")+1)],
                         mid=s[s.find("h"): s.rfind("h")].replace('h', 'H'),
                         end=s[s.rfind("h"):]))
