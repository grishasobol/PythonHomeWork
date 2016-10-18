# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:33:37 2016

@author: Gregory
"""
import random

def qsort(array, num):
    return qsort([x for x in array if x < array[num % len(array)]], num + 1) + qsort([x for x in array if x >= array[num % len(array)]], num + 1) if len(array) > 1 else array

print qsort([2, 5, 546,1, 4,45,23,786,452,8654457,12,46], 0)