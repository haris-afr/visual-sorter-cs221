import matplotlib.pyplot as plt #drawing/generating graphs
import numpy as np #used for arrays

#At certain intervals, a screenshot of the algorithm is saved using matplotlib
def take_screenshot(pictures_taken, arr, indices):
    plt.clf()
    barC = plt.bar(indices, arr, width=2/len(arr))
    plt.bar_label(barC, arr)
    plt.savefig(f"saved_figures/fig_{pictures_taken}")
    return (pictures_taken + 1)

#Sorting Algorithms 
def bubble_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    pictures_taken = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            pictures_taken = take_screenshot(pictures_taken, arr, indices)
    pictures_taken = take_screenshot(pictures_taken, arr, indices)
    return pictures_taken

def insertion_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    pictures_taken = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=-1 and key < arr[j]:
            arr[j+1] = arr[j]
            pictures_taken = take_screenshot(pictures_taken, arr, indices)
            j-=1
        arr[j+1] = key
        pictures_taken = take_screenshot(pictures_taken, arr, indices)
    print(arr)
    pictures_taken = take_screenshot(pictures_taken, arr, indices)
    return pictures_taken


def selection_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    pictures_taken = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            pictures_taken = take_screenshot(pictures_taken, arr, indices)
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        pictures_taken = take_screenshot(pictures_taken, arr, indices)
    pictures_taken = take_screenshot(pictures_taken, arr, indices)
    return pictures_taken
