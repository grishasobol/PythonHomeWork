# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:34:08 2016

@author: Gregory
"""

def qsort(lst, first, last):
    pivot = lst[first]
    l = first
    r = last
    while(r - l >= 1):
        if lst[l] >= pivot and lst[r] < pivot:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        else:
            if lst[l] < pivot:
                l += 1
            if lst[r] >= pivot:
                r -= 1
    if(l == r):
        if(lst[l] < pivot):
            r += 1
        else:
            l -= 1
    if(r - l == -1):
        r, l = l, r
    if(r == first):
        return lst    
    if(first < l):
        qsort(lst, first, l)
    if(last > r):
        qsort(lst, r, last)
    return lst
        
print qsort([213, 5453, 5463, 234, 12, 1, 90, 2453, 8546, 32478], 0, 9)   
        
    
    