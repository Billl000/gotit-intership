import math
from timeit import default_timer as timer
from random import randint
def binary_search(arr, x):
  low = 0
  high = len(arr)
  mid = math.floor((high - low) / 2)
  while True:
    if x == arr[low]:
      return (low)
    if x == arr[high-1]:
      return (high-1)

    if arr[mid] == x:
      return mid

    if (x < arr[low]) or (x > arr[high-1]):
      return -1

    if arr[mid] < x:
      low = mid
      mid += math.floor((high - low) / 2)
    else:
      high = mid
      mid -= math.floor((high - low) / 2)

  end = timer()
  print(array)
  return (end - start)
def SelectionSort(array):
  start = timer()
  for i in range(len(array)):
    k = i
    for j in range(i + 1, len(array)):
      if array[k] > array[j]:
        k = j
    array[i], array[k] = array[k], array[i]

  end = timer()
  print(array)
  return (end - start)

def BubbleSort(array):
   start = timer()
   for i in range(len(array)):
     for j in range(len(array)):
       if (array[i] < array[j]):
         array[j], array[i] = array[i], array[j]
   return array






def InsertionSort(arr):
  start = timer()
  for i in range(len(arr)):
    for j in range(i):
#      print(arr, i, j)
      if  (i == len(arr)-1):
        arr[i], arr[len(arr)-1] = arr[len(arr)-1],   arr[i]
        end = timer()
        print(arr)
        return (end - start)
      if (arr[i+1] < arr[j]):
        arr[i+1], arr[j] = arr[j], arr[i+1]

  end = timer()
  print(arr)
  return (end - start)

def quickSort(arr, x):
  low = 0
  high = len(arr) - 2
  pivot = len(arr) - 1

arr = []
for i in range(0, 100000):
  arr.append(randint(0, 100000))


print(InsertionSort(arr))
#print(binary_search(BubbleSort(arr), 8))






