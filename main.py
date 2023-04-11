#! usr/bin/env python3
from functools import reduce
from operator import truth, getitem


def keep_truthful(iterable):
    return list(filter(truth, iterable))

def abs_sum(iterable):
    return sum(list(map(abs, iterable))) # type: ignore

def walk(dct, path):  #FIX
    return reduce(getitem, dct, path)


dct = {
    'a': {
        7: {
            'b': 42
        }
    }
}

print(walk(dct, ['a', 7, 'b']))
