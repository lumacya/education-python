#! usr/bin/env python3
def count_all(iter_obj):
    final_dict = {}

    for i in iter_obj:
        final_dict[i] = iter_obj.count(i)

    return final_dict

print(count_all(['cat', 'dog', 'cat', 'cat']))
