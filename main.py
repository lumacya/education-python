#! usr/bin/env python3
def make_decart_point(x, y):
    point = {
        'x': x,
        'y': y
    }

    return point


def make_segment(start_point, end_point):
    segment = {
        'start_point': start_point,
        'end_point': end_point
    }

    return segment


def get_mid_point_of_segment(segment):
    # Can I optimize this code?
    mid_x = (segment['start_point']['x'] + segment['end_point']['x']) / 2
    mid_y = (segment['start_point']['y'] + segment['end_point']['y']) / 2
    mid_point = {
        'x': mid_x,
        'y': mid_y
    }

    return mid_point


segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
print(get_mid_point_of_segment(segment))
