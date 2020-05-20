# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # put back together, sorting happens here
    # can iterate if a sub task

    a = b = 0
    for k in range(0, elements):
        # make sure values within range
        # compare a and b
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # divides/splits data here
    # Your code here
    if len(arr) > 1:
    # stuff to left in L
        mid = len(arr) // 2
        L = merge_sort(arr[0: mid])
    # stuff to right in R
        R = merge_sort(arr[mid:])
    # find middle of r

    # merge left and right
        arr = merge(L, R)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    # re-building/sorting the dataset
    
    L = arr[start : mid+1]
    R = arr[mid+1 : end+1]
    a = b = 0
    c = start
    for k in range(c, end + 1):
        # make sure values within range
        # compare a and b
        if a >= len(L):
            arr[k] = R[b]
            b += 1
        elif b >= len(R):
            arr[k] = L[a]
            a += 1
        elif L[a] < R[b]:
            arr[k] = L[a]
            a += 1
        else:
            arr[k] = R[b]
            b += 1
    return arr

def merge_sort_in_place(arr, l, r):
    # Your code here
    # halfing the data set

    if r - l > 0:
        mid = (l+r) // 2 # double slash rounds floats down to 0dp
        # arr here 
        merge_sort_in_place(arr, l, mid)
        # arr is the original array, mid, l and r refer to the parameters required to sort it on loc 49
        merge_sort_in_place(arr, mid+1, r)
        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


# notes
# quick sort has pivot
