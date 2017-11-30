from numba import jit
import numpy as np
import time


st = time.time()*1000
x=0

@jit
def g():
    for i in range(30000000):
        x=i**2

g()
print(time.time()*1000-st)
