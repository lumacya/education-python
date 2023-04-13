#! usr/bin/env python3
def memoized(func):
    results = {}

    def wrapper(number):
        # Optimize this code
        if number in results.keys():
            return results[number]
        else:
            results[number] = func(number)
            return results[number]
        # Optimize this code

    return wrapper

@memoized
def f(x):
    print('Calculating...')
    return x * 10

print(f(10))
print(f(10))
print(f(20))
print(f(20))
print(f(10))
