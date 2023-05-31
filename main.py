#! usr/bin/env python3
from typing import Any


class Banknote:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        """__repr__ - метод для программистов, он должен возвращать строку из которой
        можно восстановить состояние объекта функцией !eval!"""
        return f'Banknote({self.value})'

    def __str__(self) -> str:
        """__str__ = метод для пользователя, просто возвращает информацию об объекте"""
        return f'Banknote: {self.value}'

    # Если __repr__ или __str__ Не реализованны, print выведет адрес объекта в памяти

    def __eq__(self, other):
        """По-умолчанию сравнивает адреса в памяти. True - если адреса одинаковые. Теперь сравнивает объекты"""
        if other is None or not isinstance(other, Banknote):
            return False
        return self.value == other.value

    # Если не реализовывать магичесике методы, то они просто не будут работать

    def __lt__(self, other):
        if other is None or not isinstance(other, Banknote):
            return f'type error'
        return self.value < other.value

    def __gt__(self, other):
        if other is None or not isinstance(other, Banknote):
            return f'type error'
        return self.value > other.value

    def __le__(self, other):
        if other is None or not isinstance(other, Banknote):
            return f'type error'
        return self.value <= other.value

    def __ge__(self, other):
        if other is None or not isinstance(other, Banknote):
            return f'type error'
        return self.value >= other.value


class Wallet:
    def __init__(self, *banknotes: Banknote) -> None:
        self.container = []
        self.container.extend(banknotes)

    def __repr__(self):
        return f'Wallet({self.container})'

    def __contains__(self, item):
        """Проверяет на in"""
        return item in self.container

    def __bool__(self):
        """Проверяет на bool"""
        if len(self.container) > 0:
            return True
        return False

    def __len__(self):
        """Возвращает длинну объекта"""
        return len(self.container)

    def __call__(self):
        """Делаеть объект callable, то есть его можно вызвать через ()"""
        return f'В кошельке {sum(i.value for i in self.container)} рублей'


if __name__ == '__main__':
    fifty = Banknote(50)
    hundred = Banknote(100)
    wallet = Wallet(fifty, hundred)
    # print(hundred in wallet)
    # if wallet:
    #     print('!')
    # else:
    #     print('empty')
    # print(len(wallet))
    print(wallet())
