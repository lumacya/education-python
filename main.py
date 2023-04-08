#! usr/bin/env python3
def greet(name, *args):
    res_string = f'Hello, {name}'

    for n in args:
        res_string += f' and {n}'

    return res_string


print(greet('Ivan'))
