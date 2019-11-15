def binary_search(A, l, h, k):
  if h >= l:
    mid = l + (h - l)/2
    if A[mid] == k:
      return 'k is found'
    elif A[mid] > k:
      return binary_search(A, l, mid-1, k)
    else:
      return binary_search(A, mid+1, h, k)
  else:
      return "k is not found"

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


def insertionSort(a):
  for i in a:
    j = a.index(i)
    while j > 0:
      if a[j - 1] > a[j]:
        a[j - 1], a[j] = a[j], a[j - 1]
      else:
        break
      j = j - 1

def mergeSort(array):

binary_search(z)





