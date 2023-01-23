# Наследование — способ создания класса. Его суть заключается в том, что функциональность нового класса наследуются от уже существующего класса. Новый класс называется производным (дочерним). Существующий — базовым (родительским).

# родительский класса
class Bird:

    def __init__(self) -> None:
        print('Птица создана')

    def who_is_this(self):
        print('Птица')

    def swim(self):
        print('Птица плывет')

# дочерний класс
class Penguin(Bird):

    def __init__(self) -> None:
        super().__init__()
        print('Пингвин готов')

    def who_is_this(self):
        print('Это пингвин')

    def run(self):
        print('Пингвин бежит')

peggy = Penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()
