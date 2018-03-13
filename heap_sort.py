# Heap Sort
def heapify(a, n, i):

    print("a = {}, n = {} and i = {}".format(a,n,i))

    largest = i
    l = 2*i + 1
    r = 2*i + 2

    print("Current root is {} with left = {} and right = {}".format(a[i], a[l] if l < n else None, a[r] if r <n else None))

    if l < n and a[l] > a[largest]:
        largest = l

    if r < n and a[r] > a[largest]:
        largest = r

    if largest != i:
        a[i],a[largest] = a[largest], a[i]
        print('\n')
        heapify(a, n, largest)

def heap_sort(a):
    n = len(a)
    print("About to heapify {}".format(a))
    for i in range(int(n/2) - 1, -1, -1):
        print('\n')
        heapify(a, n, i)
    print("\nDone! \nHeapified => {}".format(a))
    for i in range(n-1, -1, -1):
        a[0],a[i] = a[i], a[0]
        print('\n')
        heapify(a, i, 0)


a = [1,2,3,4,5,6,7,8]
heap_sort(a)
print(a)