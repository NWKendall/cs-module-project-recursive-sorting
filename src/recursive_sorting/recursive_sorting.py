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
            b+= 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # split here
    # Your code here
    if len(arr) > 1:
    # stuff to left in L
        L = merge_sort(arr[0: len(arr) // 2])
    # stuff to right in R
        R = merge_sort(arr[len(arr) // 2:])
    # find middle of r

    # merge left and right
        arr = merge(L, R)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
        


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


# notes
# quick sort has pivot
