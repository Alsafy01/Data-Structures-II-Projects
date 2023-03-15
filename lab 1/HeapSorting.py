class HeapSort:
    def __init__(self,arr,i):
        self.arr=arr
        self.i=i
        self.heapSize=self.arr.len()
    def left(i):
        return 2*i

    def right(i):
        return 2*i+1

    def parent(i):
        return i/2

    def maxHeapify(arr,i):
        l=left(arr[i])
        r=right(arr[i])
        if l<=heapSize and arr[i]<arr[l]:
            largest=l
        else:
            largest=i
        if r<=heapSize and arr[largest]<arr[r]:
            largest = r
        if largest != i:
            # exchange(arr[i],arr[largest])
            temp=arr[i]
            arr[i]=arr[largest]
            arr[largest]=temp
            MaxHeapify(arr,largest)

    def buildMaxHeap(arr):
        heapSize=arr.len()
        for j in range(arr.len()/2,1):
            MaxHeapify(arr,j)
    def heapSort(arr):
        buildMaxHeap(arr)


