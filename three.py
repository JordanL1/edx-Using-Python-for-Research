# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:37:40 2018

@author: jorda
"""

import time
import numpy as np
from matplotlib import pyplot as plt

start_time = time.clock()
X = np.random.randint(1, 7, (1000000, 10))

Y = np.sum(X, axis=1)

plt.hist(Y)
end_time = time.clock()
print(end_time - start_time)

