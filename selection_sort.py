# insertion sort

a = [9,8,1,2,3,7]

def selection_sort(a):
    n = len(a)
    i = -1
    while i < n - 1:
        k = -1
        min = float("inf")

        for j in range(i+1, n):
            if min > a[j]:
                min = a[j]
                k = j
        i += 1
        if k != -1:
            a[i],a[k] = a[k], a[i]
    return a

a = selection_sort(a)
print(a)