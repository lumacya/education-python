# FAQ - This code was written for testing "git grep" tool
def decorator(func):

    def wrapper(arg1):
        print('start decorator')
        func(arg1)
        print('end decorator')

    return wrapper

@decorator
def greet(name):
    print('Hello {}'.format(name))


greet('Ivan')
