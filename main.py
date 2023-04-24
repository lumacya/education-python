#! usr/bin/env python3
def remove_first_level(tree):
    result_list = []

    for i in tree:
        if type(i) is list:
            for k in i:
                result_list.append(k)

    return result_list

tree1 = [[5], 1, [3, 4]]
tree2 = [1, 2, [3, 5], [[4, 3, [1, 2]], 2]]

print(remove_first_level(tree2))
