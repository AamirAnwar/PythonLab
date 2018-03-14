
# Number of characters in input alphabet
D = 256
def search(pat, text, q):
    global D
    M  = len(pat)
    N = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1

    for i in range(M - 1):
        print(h)
        h = (h*D)%q

    for i in range(M):
        pattern_hash = (D * pattern_hash + ord(pat[i])) % q
        text_hash = (D * text_hash + ord(text[i])) % q
    print("{} => {}".format(pat, pattern_hash))

    print("Searching text now!")
    for i in range(N-M+1):

        print("{} => {}".format(text[i:i+M], text_hash))

        if pattern_hash == text_hash:
            print("Hash matched!")
            # Check both pattern and text one by one to confirm
            for j in range(M):
                if text[i+j] != pat[j]:
                    print("Hash matched but turned out to be not equal")
                    break
            if j == M - 1:
                print("Pattern found at {}".format(i))
                return
        else:
            if i < N-M:
                text_hash = (D * (text_hash - ord(text[i]) * h) + ord(text[i + M])) % q
                if text_hash < 0:
                    text_hash += q
    print("Pattern not found!")


def test():
    text = "maryhadalittlelamb"
    pattern = "had"
    q = 101
    search(pattern, text, q)



