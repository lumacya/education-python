class Base:
    def __init__(self, x) -> None:
        self.x = x

    def show(self):
        print(f'Base class {self.x}')

class Derivative(Base):
    def __init__(self, x) -> None:  # явный вызов конструктора
        super().__init__(x)


a = Base(10)
b = Derivative(20)
a.show()
b.show()
