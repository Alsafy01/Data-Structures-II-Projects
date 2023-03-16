import math
import random
import numpy


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def insertion_sort(array):
    a = numpy.array(array, copy=True)
    for i in range(len(a) - 1):
        while (a[i] > a[i + 1]):
            swap(a, i, i + 1)
            if (i != 0):
                i = i - 1
    return a


def selection_sort(array):
    a = numpy.array(array, copy=True)
    for i in range(len(a)):
        min = i
        for j in range(i, len(a)):
            if (a[min] > a[j]):
                min = j
        swap(a, min, i)
    return a


def merge_sort(array):
    a = list(numpy.array(array, copy=True))
    if (len(a) > 1):
        mid = len(a) // 2
        l = list(a[:mid])
        r = list(a[mid:])
        return numpy.array(merge(merge_sort(l), merge_sort(r)))
    else:
        return a


def merge(left, right):
    left_count = right_count = 0
    result = list()
    # print(left, '*****', right)
    while (left_count <= len(left) - 1 and right_count <= len(right) - 1):
        if (left[left_count] >= right[right_count]):
            result.append(right[right_count])
            right_count += 1
        else:
            result.append(left[left_count])
            left_count += 1
    if (right_count <= len(right) - 1):
        result.extend(right[right_count:])
    if (left_count <= len(left) - 1):
        result.extend(left[left_count:])
    # print(">>>", result)
    return result


def print_tree(array):
    depth = math.floor(math.log(len(array), 2))
    max_spaces = int(pow(2, depth))
    index = 0

    # for k in range(max_spaces):
    #     print('  ', end='')
    # print(" H  E  A  P")
    # for k in range(max_spaces):
    #     print('  ', end='')
    # print("\n")

    for i in range(depth + 1):
        for j in range(int(math.pow(2, i))):

            for k in range(max_spaces):
                print('  ', end='')

            print(array[index], end='')
            index += 1
            if (index >= len(array)):
                break

            for k in range(max_spaces):
                print('  ', end='')
        max_spaces = max_spaces // 2
        print("\n")


def heapify(array, size, index):
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    if (left <= size and array[largest] < array[left]):
        largest = left
    if (right <= size and array[largest] < array[right]):
        largest = right
    if (largest != index):
        swap(array, largest, index)
        heapify(array, size, largest)


def build_max_heap(array):
    a = numpy.array(array, copy=True)
    last_parent = len(a) // 2 - 1
    for i in range(last_parent, -1, -1):
        heapify(a, len(a) - 1, i)
    return a


def heap_sort(array):
    a = build_max_heap(array)
    size = len(a) - 1
    for i in range(len(a)):
        swap(a, size, 0)
        size -= 1
        heapify(a, size, 0)
    return a


def partition(array, low, high):
    pivot = random.randint(low, high)
    swap(array, pivot, high)
    pivot = high
    i = low - 1
    for j in range(low, high):
        if array[j] <= array[pivot]:
            i = i + 1
            swap(array, i, j)
    swap(array, pivot, i + 1)
    return i + 1


def quick_sort_recursion(array, low, high):
    if low < high:
        wall = partition(array, low, high)
        quick_sort_recursion(array, low, wall - 1)
        quick_sort_recursion(array, wall + 1, high)
        return array


def quick_sort(a):
    return quick_sort_recursion(numpy.array(a, copy=True), 0, len(a) - 1)


def hybrid_sort(arr):
    if len(arr) <= 10:
        return insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        leftHybrid = [x for x in arr if x < pivot]
        midHybrid = [x for x in arr if x == pivot]
        rightHybrid = [x for x in arr if x > pivot]
        return hybrid_sort(leftHybrid) + midHybrid + hybrid_sort(rightHybrid)


# def insertion_hybrid_sort(arr):
#     # for i in range(0, len(arr)):
#     key = len(arr) - 1
#     j = len(arr) - 1
#     while j >= 0:
#         if key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#             arr[j + 1] = key
#     return arr


a = numpy.random.randint(10, size=11)
print(f"Randomly Array : {a}")
print(f"Quick Sort :     {quick_sort(a)}")
print(f"Merge Sort :     {merge_sort(a)}")
print(f"Heap Sort :      {heap_sort(a)}")
print(f"Selection Sort : {selection_sort(a)}")
print(f"Insertion Sort : {insertion_sort(a)}")
print("HEAP :")
print_tree(a)
print(f"Hybrid Sort : {hybrid_sort(a)}")

