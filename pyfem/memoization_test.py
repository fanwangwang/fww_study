from tool import Memoize, Timefunc, timefunc

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

t = Timefunc(fib, 10)
t(20)

timefunc(fib, 10, number=10)

fib = Memoize(fib)
t = Timefunc(fib, 10)
t(40)

