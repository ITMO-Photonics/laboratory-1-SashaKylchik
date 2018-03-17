import math
print('enter R')
R = float (input())
print('enter L')
L = float (input())
def Area (x,y):
    a = math.pi * x * x * y
    print (a)
    return a
Area (R,L);
