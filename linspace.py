# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:55:45 2016

@author: Gregory
"""

import numpy
import time

def linspace_for(a, b, c):
    result = []
    index = a
    i = 0
    while(index <= b):
        result.append(index)
        index += (b - a) / c * i + a
        i += 1
    return numpy.array(result)

def linspace_com(a, b, c):
    return numpy.array([a + (b-a)/c*x for x in range(c)])
   
t = time.time()
print linspace_for(1, 100, 5)
print time.time() - t

t = time.time()
print linspace_com(1, 100, 5)
print time.time() - t

t = time.time()
print numpy.linspace(1, 100, 5)
print time.time() - t        