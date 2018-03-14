# Z string search

def search(text, pattern):
    search_string = pattern + "$" + text
    l = len(search_string)
    print(search_string)
    Z = getZArray(search_string)
    for i in range(1,l):
        if Z[i] == len(pattern):
            print("Pattern found at index {}".format(i - len(pattern) - 1))




def getZArray(text):
    n = len(text)
    Z = [0]*n
    L = 0
    R = 0
    for i in range(1,n):
        if i > 3:
            print("R = {} and i = {}".format(R, i))
        if i > R:
            L = i
            R = i
            print("i = {}".format(i))
            print("Starting to compare {} with {}".format(text[R-L], text[R]))
            while R < n and text[R-L] == text[R]:
                print("Comparing {} with {}".format(text[R - L], text[R]))
                R += 1
            print("Z[{}] is {}".format(i, R - L))
            Z[i] = R-L
            R -= 1
        else:
            k = i - L
            if Z[k] < R - i + 1:
                print("Z[{}] is {}".format(i , Z[k]))
                Z[i] = Z[k]
            else:
                print("Outside Z Box!")
                L = i
                while R<n and text[R-L] == text[R]:
                    R += 1
                print("Z[{}] is {}".format(i, R-L))
                Z[i] = R-L
                R -= 1
    return Z

def test():
    text = "aabcaabxaaaz"
    pattern = "bca"
    print(getZArray(text))
    # search(text,pattern)
