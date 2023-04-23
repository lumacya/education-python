#! usr/bin/env python3
def matreshka(n):
    if n == 1:
        print('Matreshechka')
    else:
        print(f'top of matreshka {n}')
        matreshka(n - 1)
        print(f'bottom of matreshka {n}')


matreshka(5)
