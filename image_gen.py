import matplotlib.pyplot as plt #drawing/generating graphs
import numpy as np #used for arrays



values = np.array([1, 10, 2, 15, 25, 4])
indices = np.array ([1, 2, 3, 4, 5, 6])


plt.ioff()
plt.draw()

def bubble_sort(vals):
    sizeA = len(vals)

    loop_called = 0
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
            plt.savefig(f"saved_figures/fig_{loop_called}")
            loop_called += 1
        if (inner_loop_called == 0):
            return loop_called
    return loop_called

#Sorting Algorithms 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            #Add screenshot here
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            #Add screenshot here
    #Final screenshot here


def insertion_sort(arr):
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
   

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            #Add screenshot here
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        #Add screenshot here
    #Final screenshot here
   
def start_Algo():
    inputArr = [int(x) for x in arrayInputLabel.get().split(',')]
    algorithm = selectedAlg.get()

    if algorithm == "Bubble Sort":
        bubble_sort(inputArr)

    elif algorithm == "Insertion Sort":
        insertion_sort(inputArr)

    elif algorithm == "Selection Sort":
        selection_sort(inputArr)

