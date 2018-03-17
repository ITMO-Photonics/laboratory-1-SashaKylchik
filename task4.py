  GNU nano 2.5.3                                  File: task4.py                                                                            

import scipy.linalg as lng 
import numpy as np
import time
N = 5
A = np.random.random((N,N))
k = np.arange(N)
b = np.zeros(N)

for t in np.linspace(0.,10.,100):
    b = k/(1.+ k * t) 
    res1 = lng.solve(A,b)
    print(res1)

lu,piv = lng.lu_factor(A)
for t in np.linspace(0.,10.,100):
    b = k/(1.+ k * t) 
    res2 = lng.lu_solve((lu,piv), b)
    print(res2)

A2 = lng.inv(A)
for t in np.linspace(0.,10.,100):
    b = k/(1.+ k * t) 
    res3 = np.dot(A2,b) 
    print(res3)

start_time =time.time()
for i in  range (10000):
    lng.solve(A,b)

print(time.time()-start_time)


start_time =time.time()
for i in  range (10000):
    lng.lu_solve((lu,piv), b)

    
print(time.time()-start_time)

start_time =time.time()
for i in  range (10000):
    np.dot(A2,b)
    
print(time.time()-start_time)
