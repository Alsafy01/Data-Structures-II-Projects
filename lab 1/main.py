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


a = numpy.random.randint(10, size=10)
print(a)
print(selection_sort(a))
print(insertion_sort(a))
print(merge_sort(a))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
