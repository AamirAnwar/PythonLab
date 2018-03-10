def _search(l,r,a,key):
    if l < r:
        m = l + int((r-l)/2)
        # print("Compaing {} with key:{}".format(a[m],key))
        # print("L : {} and R : {}".format(l,r))
        if key > a[m]:
            return _search(m + 1,r,a,key)
        elif key < a[m]:
            return _search(l,m,a,key)
        else:
            return True
    else:
        return False





def binarySearch(a,key):
    a.sort()
    return _search(0, len(a), a, key)

a = [1,2,3,4,5,6,7,8,9]
for e in a:
    print(binarySearch(a, e+10))
