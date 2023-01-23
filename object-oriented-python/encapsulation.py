# Мы можем ограничить доступ к методам и переменным, что предотвратит модификацию данных — это и есть инкапсуляция. Приватные атрибуты выделяются нижним подчеркиванием: одинарным _ или двойным __

# Используем инкапсуляцию данных
class Computer:

    def __init__(self) -> None:
        self.__maxprice = 900

    def sell(self):
        print(f'Цена продажи {self.__maxprice}')

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# Изменение цены
c.__maxprice = 950
c.sell()

# Используем функцию изменения цены
c.setMaxPrice(1000)
c.sell()
