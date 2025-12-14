# This project requires the "pandas" and "matplotlib" libraries, for .
# In case either is not installed please follow the instructions on their respective websites
# https://pandas.pydata.org/docs/getting_started/install.html   <--- pandas
# https://matplotlib.org/stable/users/getting_started/          <--- matplotlib

# the mouse library is also used, it can be installed using pip install mouse.

#-------------------------------------------------------------------------
# import pandas as pd #used for data organisation, may be redundant due to numpy
# import time
# import mouse #user input, may be redundant due to tkinter
#--------------------------------------------------------------

import matplotlib.pyplot as plt #drawing graphs
import numpy as np #used for arrays
import tkinter #GUI 


values = np.array([1, 2, 5, 6, 3, 4])
indices = np.array ([1, 2, 3, 4, 5, 6])
sizeA = len(values)

plt.ioff()
plt.draw()

#test using binary sort
for i in range(sizeA):
    inner_loop_called = 0
    for j in range(sizeA-1):
        if (values[j + 1] < values[j]):
            temp = values[j+1]
            values[j+1] = values[j]
            values[j] = temp
            inner_loop_called = 1
        plt.clf()
        plt.bar(values, indices)    
        plt.savefig(f"visual-sorter-cs221/saved_figures/fig_{i}_{j}")
        # plt.pause(0.5)
    if (inner_loop_called == 0):
        break

# plt.show()