def my_range(n):
    i = 0
    while i < n:

        yield i
        i+=1
  
for j in my_range(5):
    print(j)
