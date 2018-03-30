
import numpy as np
import scipy.optimize as opt

def f(x):
    return (np.cos(x)/(1+x**2))

a=0.1
b=2.4

if( f(a)*f(b)>0. ):
    print('Error: f(a) and f(b) should have opposite signs! Stopping.')

x=np.linspace(0.,5.,100)

brentq=opt.brentq(f,0.1,2.4)
bisect=opt.bisect(f,0.1,2.4)
newton=opt.newton(f, 0.1)



get_ipython().run_line_magic('timeit', 'opt.brentq(f,0.1,2.4) # time of brentq function processing')

get_ipython().run_line_magic('timeit', 'opt.bisect(f,0.1,2.4) # time of bisect function processing')

get_ipython().run_line_magic('timeit', 'opt.newton(f, 2.4) # time of newton function processing')
