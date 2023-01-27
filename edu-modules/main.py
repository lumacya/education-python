import greeting  # импортирование всего модуля
# если модуль большой и из него нам нужно только пару функций, то можно использовать следующий код
# from greeting import say_hi
# say_hi()

# from module_name import * - bad practice
import computation
from computation import PI, E
from computation import pi_times


greeting.say_hi()
print(greeting.name)


print(PI)
print(computation.E)
print(pi_times(3))
print(computation.pi_times(2))
