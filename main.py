#! usr/bin/env python3
def find_index(value, iter_obj):
    for index, item in enumerate(iter_obj):
        if item == value:
            return index
        else:
            continue

    return None

print(find_index(2, [1, 3, 5]))
