# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 13:47:43 2016

@author: Gregory
"""

pred_num = 1
num = 1
for i in range(3, 101, 1):
    tmp_num = num
    num += pred_num
    pred_num = tmp_num
print num
    