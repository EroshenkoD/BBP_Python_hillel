"""
2. Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов
в виде списка объектов `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь
атрибуты `name`, `age`, `grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.

Наследование здесь не понадобится.
"""


class Student:
    def __init__(self, name='Student', age=18, grades=None):
        self.__name = name
        self.__age = age
        if grades is None:
            grades = []
        self.__grades = grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        for i in grades:
            self.__grades.append(i)


class Group:
    def __init__(self, name='Group', curs=1, lst_std=None):
        self.__name = name
        self.__curs = curs
        if lst_std is None:
            lst_std = []
        self.__lst_ltd = lst_std

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def curs(self):
        return self.__curs

    @curs.setter
    def curs(self, curs):
        if curs in range(1, 6):
            self.__curs = curs
        else:
            print("Недопустимый курс")

    @property
    def lst_std(self):
        return self.__lst_ltd

    @lst_std.setter
    def lst_std(self, lst_std):
        self.__lst_ltd.append(lst_std)


s = Student('Зоя', 19, [5, 4, 4])
print(s.grades)
s.grades = [1, 1]
print(s.grades)


g = Group('Группа_1', 2,
          [Student('Иван', 19, [5, 4, 4]),
           Student('Вася', 18, [3, 4, 2]),
           Student('Петя', 20, [5, 2, 4]),
           s])

print(g.lst_std)
g.lst_std = Student('Рита', 16, [1, 2, 1])
print(g.lst_std)

g.lst_std[4].grades = [3, 3]
print(g.lst_std[4].grades)


