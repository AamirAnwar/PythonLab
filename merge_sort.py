# Merge Sort
def merge_subroutine(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0]*(n1)
    R = [0]*(n2)

    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while (i < n1 and j < n2):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k+=1

    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = R[j]
        j+=1
        k+=1


def merge_sort(l,r,a):
    if l < r:
        m = int(l + (r-l)/2)
        print("Split {} into {} and {}".format(a[l:r+1],a[l:m + 1], a[m + 1:r + 1]))
        merge_sort(l,m,a)
        merge_sort(m+1,r,a)
        print("Merging {} and {}".format(a[l:m + 1], a[m + 1:r + 1]))
        merge_subroutine(a,l,m,r)
        print("Merged into {}".format(a[l:r + 1]))

def test_merge_sort():
    a = [9,8,7,6,5,4,3,2,1]
    merge_sort(0, len(a) - 1, a)
    print("Done! => {}".format(a))


