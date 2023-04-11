#! usr/bin/env python3
def call_twice(func, *args):
    calls_list = []

    for i in range(2):
        calls_list.append(func(*args))

    return calls_list


print(call_twice(input, 'Enter a value: '))
