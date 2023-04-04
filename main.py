#! usr/bin/env python3
def rotated_left(arg):
    fisrt_elem = arg[:1]  # if type(arg) is list or tuple => arg[0] is int
    without_first = arg[1:]
    result = without_first + fisrt_elem
    return result  # if type(arg) is list or tuple => TypeError: can only concatenate list (not "int") to list

def rotated_right(arg):
    last_elem = arg[-1:]  # if type(arg) is list or tuple => arg[0] is int
    without_last = arg[:-1]
    result = last_elem + without_last
    return result


print(rotated_left((1, 2, 3, 4)))
