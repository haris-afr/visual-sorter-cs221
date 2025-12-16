import matplotlib.pyplot as plt #drawing/generating graphs
import numpy as np #used for arrays

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
            plt.clf()
            plt.bar(arr, indices)    
            plt.savefig(f"saved_figures/fig_{loop_called}")
            loop_called += 1

    plt.clf()
    plt.bar(arr, indices)    
    plt.savefig(f"saved_figures/fig_{loop_called}")
    loop_called += 1
    return loop_called

def insertion_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    loop_called = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=-1 and key < arr[j]:
            arr[j+1] = arr[j]
            #Add screenshot here
            j-=1
        arr[j+1] = key
        #Add screenshot here
    #Final screenshot here
   
insertion_sort([10, 40, 60])

def selection_sort(arr):
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    loop_called = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            #Add screenshot here
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        #Add screenshot here
    #Final screenshot here
   
# def start_Algo():
#     inputArr = [int(x) for x in arrayInputLabel.get().split(',')]
#     algorithm = selectedAlg.get()

#     if algorithm == "Bubble Sort":
#         bubble_sort(inputArr)

#     elif algorithm == "Insertion Sort":
#         insertion_sort(inputArr)

#     elif algorithm == "Selection Sort":
#         selection_sort(inputArr)

