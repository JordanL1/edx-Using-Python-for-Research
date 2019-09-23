# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:00:01 2018

@author: jorda
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 10)
y1 = x**1.5
y2 = x**2
plt.loglog(x, y1, "bx-", linewidth=2, markersize=10, label="y1")
plt.loglog(x, y2, "gx-", linewidth=2, markersize=10, label="y2")
plt.xlabel("$x$")
plt.ylabel("$y$")
#plt.axis([-1, 11, -10, 110])
plt.legend(loc="upper left")
plt.savefig("myplot.pdf")
plt.show()

x = np.random.normal(size=1000)
plt.hist(x, normed=True, bins=np.linspace(-5, 5, 21))