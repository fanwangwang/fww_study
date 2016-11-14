
import numpy as np

def unique_row(a):
    tmp = np.ascontiguousarray(a).view(np.dtype((np.void,
        a.dtype.itemsize * a.shape[1])))
    _, i, j = np.unique(tmp, return_index=True,
            return_inverse=True)
    b = a[i]
    return (b, i, j)

def myunique(a, size):
    tmpa = np.ascontiguousarray(a).view(np.dtype((np.void, 
        a.dtype.itemsize * size)))
    tmpb, i, j = np.unique(tmpa, return_index=True, 
            return_inverse=True)
    b = a[i] # TODO: fixed me
    return (b, i, j)


class Memoize:
    """  Remomber the computing result for the future using 


    """
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args]=self.f(*args)
        return self.memo[args]


class Timefunc:
    def __init__(self, f, number=10):
        self.f = f
        self.number = number

    def __call__(self, *args):
        import timeit, functools
        t = timeit.Timer(functools.partial(self.f, *args))
        print(t.timeit(self.number))

def timefunc(f, *args, **kwargs):
    import timeit, functools
    if 'number' in kwargs.keys():
        number = kwargs['number']
    else:
        number = 10
    t = timeit.Timer(functools.partial(f, *args))
    print(t.timeit(number))
    

