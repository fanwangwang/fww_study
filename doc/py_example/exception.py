import sys
n = int(sys.argv[1])
try:
    print(1.0/n)
except ZeroDivisionError:
    print('no reciprocal')
