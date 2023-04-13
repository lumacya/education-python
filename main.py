#! usr/bin/env python3
def make_module(step=1):
    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}


m = make_module(step=2)
print(m['inc'] (10))
