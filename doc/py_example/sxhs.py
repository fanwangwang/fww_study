def sxhs(a,b,c):
    for i in range(1,11):
        for j in range(0,11):
            for k in range(0,11):
                d = 100*i + 10*j + k
                f = i**3 + j**3 + k**3
                if d ==f:
                    print(i,j,k)
                    print(f)
    return sxhs

s = sxhs(2,2,5)


