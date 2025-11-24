# This project requires the "pandas" and "matplotlib" libraries.
# In case either is not installed please follow the instructions on their respective websites
# https://pandas.pydata.org/docs/getting_started/install.html   <--- pandas
# https://matplotlib.org/stable/users/getting_started/          <--- matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter
import time

a = np.array([1, 2, 5, 6, 3, 4])
b = np.array ([1, 2, 3, 4, 5, 6])
sizeA = len(a)
plt.bar(a, b)
#test using binary sort
for i in range(sizeA):
    for j in range(sizeA-1):
        if (a[j + 1] < a[j]):
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
        plt.clf()
        plt.draw()
        plt.pause(0.5)

plt.ioff()
plt.show()
