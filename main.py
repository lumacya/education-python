#! usr/bin/env python3
import math


def get_square_roots(number):
    """Returns the square roots of a number"""
    result_list = []

    if number < 0:
        result_list.append('None')  # No roots
        return result_list

    elif number == 0:
        zero = int(math.sqrt(number))  # Zero has only one root - zero
        result_list.append(zero)
        return result_list

    else:
        # Returns two roots. The first is negative, the second is positive
        positive_root = round(math.sqrt(number), 2)
        negative_root = -positive_root
        result_list.extend([negative_root, positive_root])
        return result_list


def get_range():
    pass


print(get_square_roots(9))
