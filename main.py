#! usr/bin/env python3
def count():
    counter = 0

    def inner(value):
        nonlocal counter
        counter += value
        return counter

    return inner


if __name__ == '__main__':
    cnt = count()
    print(cnt(1))
    print(cnt(2))
    print(cnt(-3))
