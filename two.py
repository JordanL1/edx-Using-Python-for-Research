# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:08:18 2018

@author: jorda
"""

import time
import random
from matplotlib import pyplot as plt

start_time = time.clock()
ys = []

for i in range(1000000):
    y = 0
    for j in range(10):
        x = random.choice([1, 2, 3, 4, 5, 6])
        y = y + x
    ys.append(y)
    
plt.hist(ys)
end_time = time.clock()
print(end_time - start_time)