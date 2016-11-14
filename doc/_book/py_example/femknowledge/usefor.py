# 使用`for`循环 
# 给定一个函数 $f(x) = x*x + x + 1$ ,求从0到n的值以及他们的和

def f(x):
    f = x*x + x + 1
    return f
s = 0
for i in range(5):
    s += f(i)
    print(f(i),s)
