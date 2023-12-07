class Person:
     def __init__(self, name='', age=0):
        self.__name = name
        self.__age = age
     def say(self):
        return "Hi :)"
     def __str__(self):
        return "Person {} is {} years old".\
            format(self.__name, self.__age)
     def get_name(self):
        return self.__name
     def get_age(self):
        return self.__age
     def set_name(self, name):
        self.__name = name
     def set_age(self, age):
        self.__age = age


class Student(Person):
    def __init__(self, name, age, avrege_degre=0):
        super(Student, self).__init__(name, age)

        self.__avrege_degre = avrege_degre

    def    get_avrege_degre(self):
        return self.__avrege_degre

    def    set_avrege_degre(self, avrege_degre):
        self.__avrege_degre = avrege_degre

    def __str__(self):
        return f"student name  {self.get_name()} is {self.get_age()} years old and his " \
               f"avrege_degre {self.__avrege_degre}"

    def say(self):
        return "Hi everybody:)"

class CyberStudent(Student):
    def __init__(self, name, age, avrege_degre, cyber_grade):
        super(CyberStudent, self).__init__(name, age, avrege_degre)

        self.__cyber_grade = cyber_grade

    def get_cyber_grade(self):
        return self.__cyber_grade