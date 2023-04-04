#! usr/bin/env python3
def rotate(lst):
    if len(lst) == 0:
        return lst
    else:
        lst.insert(0, lst.pop())
        return lst

lst = [1, 2, 3, 4]
print(rotate(lst))
