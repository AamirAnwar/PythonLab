
# Quicksort

def partition(l,r,a):
    p = a[r]
    i = l - 1
    for j in range(l,r):
        if a[j] <= p:
            i += 1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r], a[i+1]
    return i+1


def quick_sort(l,r,a):
    if l < r:
        m = partition(l,r,a)
        quick_sort(l,m - 1,a)
        quick_sort(m+1,r,a)


a = [9,8,7,6,5,4,3,2,1]
quick_sort(0,len(a) - 1,a)
print(a)