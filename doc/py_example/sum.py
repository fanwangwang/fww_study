import numpy as np

def f(a,b,c):
    return a+b+c
s1 = 0
s2 = 0
s3 = 0
n = 101
m = 51
s = 11
for i in range(n):
    s1 = s1 + i
print(s1)
for j in range(m):
    s2 = s2 + j*j
print(s2)
for k in range(1,s):
    s3 = s3 + 1.0/k
print(s3)

sum = f(s1,s2,s3)
print(sum)
