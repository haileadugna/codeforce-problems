# implement insertion for tries
class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False


class Tries:

    def  __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word:str) :
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord
    
    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]

        return True
    

