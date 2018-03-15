
# Runs in O(n*n!)
# Takes linear time to print a permutation
def print_permutations(text , i = 0):
    n = len(text)
    if n - i - 1 > 0:
        for j in range(i,n):
            t = list(text)
            t[i],t[j] = t[j],t[i]
            t = ''.join(t)
            print_permutations(t,i+1)
    else:
        print(text)



def test():
    text = "ABCDE"
    print_permutations(text)
