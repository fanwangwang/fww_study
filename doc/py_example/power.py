def f(x,r,n):
    for i in range(n):
        x = x*r
    print(x)
    return f

f(1,3,4)
