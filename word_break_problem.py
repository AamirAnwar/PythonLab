

def word_break(text,dict):
    if len(text) == 0: return True
    n = len(text)
    for i in range(1, n+1):
        prefix = text[0:i]
        if prefix in dict:
            print("Considering {}".format(prefix))
            suffix = text[i:]
            print("Suffix => {}".format(suffix))
            if word_break(suffix,dict):
                print("{} found !".format(prefix))
                print("Rest of the string is {}".format(text[i:]))
                return True
    return False


def test():
    dict = ["mobile","samsung","sam","sung", "man","mango","icecream","and","go","i","like","ice","cream"]
    # print(dict)
    text = "mobilesamicesamsungsamsungsungsungicecreamicecream"
    print(word_break(text,dict))
