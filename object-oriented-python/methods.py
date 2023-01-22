# Методы — функции, объявленные внутри тела класса. Они определяют поведения объекта.

class Parrot():

    # атрибуты экземпляра класса
    def __init__(self, name, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color

    # метод экземпляра класса
    def sing(self, song):
        return '{} - поет {}'.format(self.name, song)

    # метод экземпляра класса
    def dance(self, dance):
        return '{} - танцует {}'.format(self.name, dance)

# создаем экземпляр класса
kesha = Parrot('Kesha', 2, 'Reg-Green')

# вызываем методы экземпляра
print(kesha.sing('XO Tour Lif3'))
print(kesha.dance('Samba'))
