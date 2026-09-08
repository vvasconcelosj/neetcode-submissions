class PrefixNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def has(self, c):
        return c in self.children

    def add(self, c):
        self.children[c] = PrefixNode()

    def get_children(self, c):
        return self.children[c]

    def set_word(self):
        self.word = True

    def is_word(self):
        return True == self.word

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if not curr.has(c):
                curr.add(c)
            
            curr = curr.get_children(c)
        
        curr.set_word()

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if not curr.has(c):
                return False

            curr = curr.get_children(c)

        return curr.is_word()
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if not curr.has(c):
                return False

            curr = curr.get_children(c)

        return True
        
        