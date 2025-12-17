#Custom sorter, simply write the algorithm you want in between the comments
#and take screenshots everytime something changes, then run it form the custom setting
#in the main program
import numpy as np
from image_gen import take_screenshot



def custom_sort(arr):
    pictures_taken = 0
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])

    #copy paste this line when taking a picture
    pictures_taken = take_screenshot(pictures_taken, arr, indices)

    #write code here-----

    #--------------------

    return pictures_taken