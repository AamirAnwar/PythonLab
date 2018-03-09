a = [9,8,1,2,3,7]

a = [9,8,1,2,3,7]

def insertion_sort(a):
    n = len(a)
    for i in range(n - 1):
        j = i + 1
        while j > 0 and a[j-1] > a[j]:
            a[j-1],a[j] = a[j], a[j-1]
            j -= 1
        i += 1
    return a

a = insertion_sort(a)
print(a)
