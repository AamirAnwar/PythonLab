def gen(txt, current, length, start):
    if len(current) >= length:
        print(current)
        return

    for k in range(start, len(txt)):
        t = current + txt[k]
        # print("t is now {}".format(t))
        gen(txt, t, length, k+1)



def printCombinations(text):
    txt = list(text)
    n = len(txt)
    for l in range(1,n+1):
        gen(txt, '', l, 0)

printCombinations("abc")