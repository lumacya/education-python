# Перегрузка оператора — это возможность переопределять различные операторы в классах, то есть менять операции, которые они выполняют, в зависимости от контекста.

# Например, оператор + в зависимости от типа операндов может складывать 2 числа, сливать 2 списка или объединять 2 строки.

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Перегрузка оператора +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # Перегрузка оператора "меньше чем"
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(1, 2)
p2 = Point(2, 3)

# print(p1 + p2)  # TypeError до перегрузки оператора +

# print(p1)  # <__main__.Point object at 0x7fe647f3fc10>

print(p2)

print(p1 + p2)  # после перегрузки оператора +
print(p1 < p2)
print(p2 < p1)
