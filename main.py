#! usr/bin/env python3
def filter_map(function, iter_object):
    mapped = list(map(function, iter_object))
    filtered = []

    for item in mapped:
        if item[0] == True:
            filtered.append(item[1])

    return filtered



def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


lst = [1, 0, 5, -5, 2]

for s in filter_map(make_stars, lst):
    print(s)
