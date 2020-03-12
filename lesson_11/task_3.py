"""
3. Дан словарь ключами которого являются английские слова, а занчениями - списки латинских слов. Необходимо развеннуть
словарь. Другими словани, необходимо, на основании заданного словаря, создать новый словарь, у которого в качестве
ключей будут взяты латинские слова, из первого словаря, а значениями будут, соответствующие им, английские слова.
d = {
    	'apple': ['malum', 'pomum', 'popula'],
    	'fruit': ['baca', 'bacca', 'popum'],
    	'punishment': ['malum', 'multa']
}

"""

d = {'apple': ['malum', 'pomum', 'popula'], 'fruit': ['baca', 'bacca', 'popum'], 'punishment': ['malum', 'multa']}
d_2 = {}

all_list = []
for key, value in d.items():
    for param in d[key]:
        if param not in d_2:
            d_2[param] = [key]
        else:
            d_2[param].append(key)

for key, value in d_2.items():
    print(key, '-', value)
