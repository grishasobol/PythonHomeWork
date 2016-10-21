# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:31:13 2016

@author: Gregory
"""

import matplotlib.pyplot as plt
from math import *
import numpy as np

from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')

plt.figure(1)
plt.subplot(1, 2, 1)
sett = np.arange(0, 5, 0.05)
plt.plot(sett, [sin(x) for x in sett], sett, [x for x in sett], sett, [sqrt(x) for x in sett])
plt.xlabel(r'\textbf{time} (s)')
plt.ylabel(r'\textit{voltage} (mV)',fontsize=16)

plt.subplot(1, 2, 2)
sett = np.arange(0, 5, 0.05)
plt.plot(sett, [sin(x) for x in sett], sett, [x for x in sett], sett, [sqrt(x) for x in sett])
plt.xlabel(r'\textbf{time} (s)')
plt.ylabel(r'\textit{voltage} (mV)',fontsize=16)

plt.savefig('tex_demo')
plt.show()
