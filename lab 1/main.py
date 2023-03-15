import numpy


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def insertion_sort(array):
    a = numpy.array(array, copy=True)
    for i in range(len(a)-1):
        while(a[i] > a[i+1]):
            swap(a, i, i+1)
            if(i != 0):
                i = i-1
    return a


def selection_sort(array):
    a = numpy.array(array, copy=True)
    for i in range(len(a)):
        min = i
        for j in range(i, len(a)):
            if(a[min]> a[j]):
                min = j
        swap(a, min, i)
    return a


def merge_sort(array):
    arr = numpy.array(array, copy=True)
    a = list(arr)
    if(len(a) > 1):
        mid = len(a) // 2
        l = a[:mid]
        r = a[mid:]
        return  merge(merge_sort(l), merge_sort(r))
    else:
        return a

def merge(left, right):
    left_count = right_count = 0
    result = list()
    #print(left, '*****', right)
    while(left_count <= len(left) - 1 and right_count <= len(right) - 1):
        if(left[left_count] >= right[right_count]):
            result.append(right[right_count])
            right_count += 1
        else:
            result.append(left[left_count])
            left_count +=1
    if(right_count <= len(right) - 1):
        result.extend(right[right_count:])
    if(left_count <= len(left) - 1):
        result.extend(left[left_count:])
    #print(">>>", result)
    return result

# def left(i: int):
#     return 2*i
#
# def right(i):
#     return 2*i+1
#
# def parent(i):
#     return i/2
#
# def maxHeapify(array,i):
#     arr = numpy.array(array, copy=True)
#     heapSize=len(arr)
#     l=left(i)
#     r=right(i)
#     if l<=heapSize and arr[i]<arr[l]:
#         largest=l
#     else:
#         largest=i
#     if r<=heapSize and arr[largest]<arr[r]:
#         largest = r
#     if largest != i:
#         # exchange(arr[i],arr[largest])
#         # temp=arr[i]
#         # arr[i]=arr[largest]
#         # arr[largest]=temp
#         swap(arr,i,largest)
#         maxHeapify(arr,largest)
#
# def buildMaxHeap(array):
#     arr = numpy.array(array, copy=True)
#     heapSize=len(arr)
#     for j in range(int(len(arr)/2) ,1,-1):
#         maxHeapify(arr,j)
# def heapSort(array):
#     arr = numpy.array(array, copy=True)
#     buildMaxHeap(arr)
#     for i in range(int(len(arr)),2,-1):
#         swap(arr,0,i)
#         heapSize=heapSize-1
#     maxHeapify(arr,0)
#     return arr

a = numpy.random.randint(10, size=10)
heapSize=len(a)
print("a is ", a)
print("selection_sort(a) is", selection_sort(a))
print("insertion_sort(a) is", insertion_sort(a))
print("merge_sort(a) is ", merge_sort(a))
# print("heapSort is", heapSort(a))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
