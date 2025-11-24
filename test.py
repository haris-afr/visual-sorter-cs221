# This project requires the "pandas" library.
# In case it is not installed please follow the instructions on the pandas website
# https://pandas.pydata.org/docs/getting_started/install.html

import pandas as pd
import tkinter

a = [1, 2, 5, 6, 3]
sizeA = len(a)
va1 = pd.Series(a)
print(va1)

for i in range(sizeA):
    for j in range(sizeA-1):
        if (va1[j + 1] < va1[j]):
            temp = va1[j+1]
            va1[j+1] = va1[j]
            va1[j] = temp

print (va1)