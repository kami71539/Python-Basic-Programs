'''print(10+2*3)
print(10-2*3)
print(10/3*5)
print(10%3*5)
print(10*2*3)
print(pow(2,3))
print(max(10,20))
print(abs(-3))
print(round(3.6))
from math import*
print(floor(4.8))
print(ceil(4.2))
print(sqrt(9))'''
def cbrt(x):
    for i in range(x):
        if(i*i*i==x):
            return i
    return "No Cube root"
print(cbrt(8))