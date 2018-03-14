# KMP Search O(m+n)



def kmp_search(pat, txt):
    M = len(pat)
    N = len(txt)

    lps = [0]*M
    compute_lps_array(pat,M,lps)
    i = 0
    j = 0
    while i < N:
        if pat[j] == txt[i]:
            j += 1
            i += 1

        if j == M:
            print("Pattern Found! at index {}".format(i - j))
            j = lps[j - 1]
        elif  i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def compute_lps_array(pat, M, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


def test_KMP():
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    kmp_search(pat,txt)


