# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:42:24 2016

@author: Gregory
"""

from numpy import *
from time import *
from random import *


def list_generate(num):
    list = []
    for i in range(num):
        list.append(randint(1, 1000000))
    return list
    
list = list_generate(1000000)
arr = asarray(list)
t = time()
arr.sort()
print 'ndarray: %f' % (time() - t),
t = time()
list.sort()
print 'list: %f' % (time() - t)