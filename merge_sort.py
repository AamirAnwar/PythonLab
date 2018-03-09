# Merge Sort
def merge_subroutine(a,b):
    # print("Merging {} and {}".format(a,b))
    i = 0
    j = 0
    total_length = len(a) + len(b)
    c = [0]*total_length
    k = 0
    while i < len(a) or j < len(b):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                c[k] = a[i]
                i += 1
            elif a[i] >= b[j]:
                c[k] = b[j]
                j += 1
        else:
            if i < len(a):
                for counter in range(i,len(a)):
                    c[k] =  a[counter ]
                    k += 1
                i = len(a)
            elif j < len(b):
                for counter in range(j,len(b)):
                    c[k] =  b[counter]
                    k += 1
                j = len(b)
        k = k + 1
    # print("Merged C = {}".format(c))
    return c

def merge_sort(l,r,a):
    if l >= r:
        return a[l:r+1]
    m = int(l + (r-l)/2)

    sub_l = list(a[l:m + 1])
    sub_r = list(a[m + 1:r + 1])
    # print("Splitting!{} into {} | {}".format(a[l:r + 1], sub_l, sub_r))
    sub_a = merge_sort(l,m,a)
    sub_b = merge_sort(m+1,r,a)
    return merge_subroutine(sub_a, sub_b)


a = [9,8,7,2,3,1,23, -1,-2,-3,-6,-7,33,55,77]
print(merge_sort(0, len(a) - 1, a))


