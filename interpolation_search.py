# Interpolation search O(log(log(n))) :Og

def interpol_search(a, x):
    l = 0
    r = len(a) - 1
    while l <= r and x >= a[l] and x <= a[r]:
        pos = l + int(((r-l)/(a[r] - a[l]))*(x - a[l]))
        if a[pos] == x:
            return pos
        if a[pos] < x:
            l = pos+1
        else:
            r = pos - 1
    return -1


a = [9,8,7,6,5,4,3,2,1]
a.sort()
print("Searching in {}".format(a))
print(interpol_search(a, 8))

