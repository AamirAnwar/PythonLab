

def checkPalindrome(s):
    n = len(s)
    i = 0
    j = n-1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if i < j:
        return False
    else:
        return True



def addStrings(v, s, temp, index):
    length = len(s)
    current = temp
    str = ''

    # print(current)
    if index == 0:
        temp = []
    for i in range(index,length):
        str = str + s[i]

        if checkPalindrome(str):
            print("Found a palindrome {}".format(str))
            temp.append(str)
            print(temp)
            if (i+1)<length:
                addStrings(v,s,temp,i+1)
            else:
                print("Reached the end! with Temp = {}".format(temp))
                v.append(list(temp))
            print("Temp is now {}".format(current))
            if len(current):
                current.pop()
            temp = current
        else:
            print("Not a palindrome {}".format(str))



def partition(text):
    temp = []
    v = []
    addStrings(v,text,temp,0)
    print(v)

def test():
    text = "geeks"
    # print(checkPalindrome("D"))
    partition(text)
