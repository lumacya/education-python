#! usr/bin/env python3
import math

def calculate_distance(point1, point2):
    x_a, y_a = point1
    x_b, y_b = point2
    distance = math.sqrt(((x_b - x_a) ** 2) + ((y_b - y_a) ** 2))
    return distance

point1 = [0, 0]
point2 = [3 ,4]
print(calculate_distance(point1, point2))
