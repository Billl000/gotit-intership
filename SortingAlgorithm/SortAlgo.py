from bisect import bisect_left
def SelectionSort(array):
    for i in range(len(array)):
        k = i
        for j in range(i + 1, len(array)):
            if array[k] > array[j]:
                k = j
        array[i], array[k] = array[k], array[i]
    print("Sorted array")
    for i in range(len(array)):
        print("%d" % array[i])

def InsertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def quickSort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return array


def binarySearch(arr, l, r, x):
#    l = arr[0]
#    r = arr[len(arr) - 1]
    if r >= l:
        mid = round(l + (r - l) / 2)

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        return -1





def binarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        print(("The number %d is the %dth item in the array" % (x, i)))
    else:
        return -1



print(binarySearch(bubbleSort([4, 6, 2, 3, 1, 5]), 7))



