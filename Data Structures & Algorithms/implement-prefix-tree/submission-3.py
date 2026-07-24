class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        recent = self.root
        for char in word:
            if char not in recent.children:
                recent.children[char] = TrieNode()
            
            recent = recent.children[char]
        
        recent.wordEnd = True


    def search(self, word: str) -> bool:
        recent = self.root
        for char in word:
            if char not in recent.children:
                return False
            
            recent = recent.children[char]
        
        return recent.wordEnd
        

    def startsWith(self, prefix: str) -> bool:
        recent = self.root
        for char in prefix:
            if char not in recent.children:
                return False
            
            recent = recent.children[char]
        
        return True

        
        