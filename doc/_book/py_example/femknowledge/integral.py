# 给定一个一维函数 $f(x) = x^2 + x + 1$, 计算它的在 [0,1] 区间上的Gauss 积分? 

def f(x):
    f = x*x + x + 1
    return f
a = 0
b = 1
def g(t):
    g = f((a+b)/2+(b-a)/2*t) 
    return g

Gi1 = (b-a)/2*2*g(0)
print(Gi1)
Gi2 = (b-a)/2*(1*g(0.5773502692)+1*g(-0.5773502692))
print(Gi2)
Gi3 = (b-a)/2*(5/9*g(0.7745906692)+8/9*g(0.0)+5/9*g(-0.7745906692))
print(Gi3)
