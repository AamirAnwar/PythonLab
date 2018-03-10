# counting sort

def count_sort(a , r):
    count_list = [0]*r
    for e in a:
        count_list[e] += 1
    for j in range(1,len(count_list)):
        count_list[j] += count_list[j-1]
    op = [0]*(len(a))
    for e in a:
        index = count_list[e] - 1
        count_list[e] -= 1
        if index > -1 and index < len(op):
            op[index] = e
    return op

a = [1,4,1,2,7,5,2,55,34,76,11,56,8,34,7,12,5]
# a = [1,4,1,2,7,5,2]
print(count_sort(a, 77))