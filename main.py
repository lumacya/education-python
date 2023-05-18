#! usr/bin/env python3
class Person:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f'Name: {self.__name}')


class Employee(Person):
    def __init__(self, name, company) -> None:
        super().__init__(name)
        self.__company = company

    def display_info(self):
        super().display_info()
        print(f'Company: {self.__company}')

    def work(self):
        print(f'{self.name} works')


tom = Employee('Thomas', 'Microsoft')
print(tom.name)
