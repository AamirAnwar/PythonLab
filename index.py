
print("Welcome to Python Lab!")

'''
The Python Playground!
'''
# Trie data structure

class Node:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):

        # Start at root of trie
        p = self.root

        # Get length of query string
        length = len(key)
        '''
         For each letter in the query check if the
         trie contains it's prefix recursively.
         If it doesn't create a node at that level.
        '''

        for level in range(length):
            index = self._charToIndex(key[level])
            if not p.children[index]:
                p.children[index] = Node()
            p = p.children[index]
        p.isEndOfWord = True

    def search(self, key):
        p = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not p.children[index]:
                return False
            p = p.children[index]
        return p != None and p.isEndOfWord

# driver function
def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "answer", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    searchKeys = ["the", "these", "their", "thaw", "a"]
    for s in searchKeys:
        print("{} ---- {}".format(s, output[t.search(s)]))



main()