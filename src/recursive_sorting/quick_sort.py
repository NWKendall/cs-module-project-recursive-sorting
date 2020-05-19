# not in place = mem intensive, less efficient
def partition(data):
    # pick first el to be pivot (can be random)
    pivot = data[0]
    L = []
    R = []

    for x in data[1:]:
        if x <= pivot:
            L.append(x)
        else:
            R.append(x)
    
    return L, pivot, R

def quick_sort(data):
    # base case
    if len(data) == 0:
        return data
    # base case
    if len(data) == 1:
        return data
    
    L, pivot, R = partition(data)

    return quick_sort(L) + [pivot] + quick_sort(R)


##############################################################################

# in palce = more memory efficient
# swapping elements in array rather than initializing sub arrays

def ip_partition(data, start, end):
    # pick first el to be pivot (can be random)
    pivot = data[start]

    i = start + 1
    j = start + 1

    # partitioning step to move elements round the pivot
    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1

    data[start], data[i-1] = data[i-1], data[start]

    return i -1

def ip_quick_sort(data, start=0, end=None):
    # base case
    if end is None:
        end = len(data) - 1
    if start == end:
        return
    
    # returns index of pivot
    index = ip_partition(data, start, end)

    # L of Pivot
    ip_quick_sort(data, start, index - 1)
    # R of Pivot
    ip_quick_sort(data, index + 1, end)
