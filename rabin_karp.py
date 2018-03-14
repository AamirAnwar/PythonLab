
# Number of characters in input alphabet
D = 256
d = 256

# def _search(pat, txt, q):
#     M = len(pat)
#     N = len(txt)
#     i = 0
#     j = 0
#     p = 0  # hash value for pattern
#     t = 0  # hash value for txt
#     h = 1
#
#     # The value of h would be "pow(d, M-1)%q"
#     for i in range(M - 1):
#         h = (h * d) % q
#
#     # Calculate the hash value of pattern and first window
#     # of text
#     for i in range(M):
#         p = (d * p + ord(pat[i])) % q
#         t = (d * t + ord(txt[i])) % q
#
#     # Slide the pattern over text one by one
#     for i in range(N - M + 1):
#         # Check the hash values of current window of text and
#         # pattern if the hash values match then only check
#         # for characters on by one
#         if p == t:
#             # Check for characters one by one
#             for j in range(M):
#                 if txt[i + j] != pat[j]:
#                     break
#
#             j += 1
#             # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
#             if j == M:
#                 print ("Pattern found at index {}".format(i))
#
#         # Calculate hash value for next window of text: Remove
#         # leading digit, add trailing digit
#         if i < N - M:
#             t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
#
#             # We might get negative values of t, converting it to
#             # positive
#             if t < 0:
#                 t = t + q

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



