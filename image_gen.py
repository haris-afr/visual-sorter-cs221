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
        while j>=0 and key < arr[j]:
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

def mergeSort (arr):
    arr = np.array(arr)
    indices = np.array([i+1 for i in range(len(arr))])
    loop_called = 0

    if len (arr) > 1:
        mid = len (arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort (L)
        mergeSort (R)

        i = j = k = 0

        while i < len (L) and j < len (R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                loop_called = take_screenshot(loop_called, arr, indices)
            else:
                arr[k] = R[j]
                j += 1
                loop_called = take_screenshot(loop_called, arr, indices)
            k += 1

        while i < len (L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len (R):
            arr[k] = R[j]
            j += 1
            k += 1

        loop_called = take_screenshot(loop_called, arr, indices)

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

