"""
1. По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

Например:
50      1 4 9 16 25 36 49
10      1 4 9
9       1 4 9
4       1 4
1       1
100     1 4 9 16 25 36 49 64 81 100
99      1 4 9 16 25 36 49 64 81

"""

N = int(input("Укажите целое число: "))

i = 1

while True:
    if not N:
        print(0)
        break
    print(i*i)
    i += 1
    if (i*i) > N:
        break
