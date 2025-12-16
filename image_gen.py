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

