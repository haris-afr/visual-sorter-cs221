import matplotlib.pyplot as plt #drawing/generating graphs
import numpy as np #used for arrays

def take_screenshot(loop_called, arr, indices):
    plt.clf()
    barC = plt.bar(indices, arr, width=2/len(arr))
    plt.bar_label(barC, arr)
    plt.savefig(f"saved_figures/fig_{loop_called}")
    return (loop_called + 1)

#Sorting Algorithms 
def bubble_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    loop_called = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            loop_called = take_screenshot(loop_called, arr, indices)
    loop_called = take_screenshot(loop_called, arr, indices)
    return loop_called

def insertion_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    loop_called = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            loop_called = take_screenshot(loop_called, arr, indices)
            j-=1
        arr[j+1] = key
        loop_called = take_screenshot(loop_called, arr, indices)
    loop_called = take_screenshot(loop_called, arr, indices)
    return loop_called


def selection_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    loop_called = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            loop_called = take_screenshot(loop_called, arr, indices)
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        loop_called = take_screenshot(loop_called, arr, indices)
    loop_called = take_screenshot(loop_called, arr, indices)
print(bubble_sort([9, 8, 7, 6, 10, 2]))