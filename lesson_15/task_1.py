"""
1. Реализовать класс цифрового счетчика. Обеспечьте возможность установки максимального и минимального значений,
 увеличения счетчика на 1, возвращения текущего значения.
"""


class counter:
    def __init__(self, start=0, end=1):
        self.__start = start
        self.__end = end
        self.__cur_pos = start
        self.__step = 1

    @property
    def cur_pos(self):
        return self.__cur_pos

    def next_pos(self):
        if self.__cur_pos == self.__end:
            self.__cur_pos = self.__end
            print('Счетчик достиг своего лимита.')
        else:
            self.__cur_pos = self.__cur_pos + self.__step

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        if start >= self.__end:
            print('Не допустимое значение старта счетчика')
        else:
            self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        if end - self.__step <= self.__start:
            print('Не допустимое значение окончания счетчика')
        else:
            self.__end = end


s = 0
e = 10
cnt = counter()
cnt.start = s
cnt.end = e
print('Начало счетчика: {}'.format(cnt.start))
print('Окончание счетчика: {}'.format(cnt.end))
print('Текущие положение счетчика: {}'.format(cnt.cur_pos))

while True:
    cnt.next_pos()
    print(cnt.cur_pos)
    if cnt.cur_pos == cnt.end:
        break

cnt.next_pos()

cnt.start = e
cnt.end = s






