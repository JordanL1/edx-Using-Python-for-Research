# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:46:04 2018

@author: jorda
"""

import numpy as np
from matplotlib import pyplot as plt

X_0 = np.array([[0], [0]])
delta = np.random.normal(0, 1, (2,1000))
Xt = np.cumsum(delta, axis=1)

X = np.concatenate((X_0, Xt), axis=1)

plt.plot(X[0], X[1], "ro-")
plt.savefig("rw.pdf")