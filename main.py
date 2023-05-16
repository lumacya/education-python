#! usr/bin/env python3
class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')


tom = Person('Thomas', 'Shelby')
tom.full_name = 'Alice Cooper'
print(tom.full_name)
