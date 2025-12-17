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
    return loop_called

def mergeSort_front(arr):
    """The function main.py calls."""
    arr = np.array(arr)
    n = len(arr)
    indices = np.array([i+1 for i in range(n)])
    loop_called = 0

    loop_called = take_screenshot(loop_called, arr, indices)
    
    # Start the recursion on the full array
    loop_called = mergeSort_back(arr, 0, n - 1, indices, loop_called)
    
    # Final 'sorted' screenshot
    loop_called = take_screenshot(loop_called, arr, indices)
    return loop_called

def mergeSort_back (arr, low, high, indices, loop_called):
    if low < high:
        mid = (low + high) // 2
        
        # Recursively sort halves
        loop_called = mergeSort_back(arr, low, mid, indices, loop_called)
        loop_called = mergeSort_back(arr, mid + 1, high, indices, loop_called)
        
        # Merge the sorted halves
        loop_called = merge(arr, low, mid, high, indices, loop_called)
        
    return loop_called

def merge(arr, low, mid, high, indices, loop_called):
    # Create temporary copies of the sub-arrays
    left_part = arr[low : mid + 1].copy()
    right_part = arr[mid + 1 : high + 1].copy()
    
    i = 0 # pointer for left_part
    j = 0 # pointer for right_part
    k = low # pointer for the original 'arr'
    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        
        # Take a screenshot of the WHOLE array after every single placement
        loop_called = take_screenshot(loop_called, arr, indices)
        k += 1
        
    # Clean up remaining elements
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
        loop_called = take_screenshot(loop_called, arr, indices)
        
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1
        loop_called = take_screenshot(loop_called, arr, indices)
        
    return loop_called

# Binary Search Tree 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_coords(node, x, y, dx):
    if not node: return [], []
    coords = [(x, y, node.val)]
    lines = []
    if node.left:
        lines.append(((x,y), (x-dx, y-1)))
        c, l = get_coords(node.left, x-dx, y-1, dx/2)
        coords += c
        lines += l
    if node.right:
        lines.append(((x,y), (x+dx, y-1)))
        c, l = get_coords(node.right, x+dx, y-1, dx/2)
        coords += c
        lines += l
    return coords, lines

def bst_sort(arr):
    arr = np.array(arr)
    root = None
    loop_called = 0
    for num in arr:
        if not root:
            root = TreeNode(num)
        else:
            curr = root
            while True:
                if num < curr.val:
                    if curr.left is None:
                        curr.left = TreeNode(num)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = TreeNode(num)
                        break
                    curr = curr.right

        plt.clf() 
        plt.axis('off') 
        coords, lines = get_coords(root, 0, 0, 4)
        for p1, p2 in lines:
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', zorder=1)
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        plt.scatter(xs, ys, s=1000, c='skyblue', edgecolors='black', zorder=2)
        for x, y, val in coords:
            plt.text(x, y, str(val), ha='center', va='center', fontweight='bold', zorder=3)
        plt.savefig(f"saved_figures/fig_{loop_called}.png")
        loop_called += 1
    return loop_called

