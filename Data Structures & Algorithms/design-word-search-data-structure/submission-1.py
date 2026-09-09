class WordNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = WordNode()

            curr = curr.children[c]

        curr.word = True
        

    def search(self, word: str) -> bool:
    
        def backtrack(node, i):

            if i == len(word):
                return node.word

            c = word[i]

            if c == '.':
                for child in node.children.values():
                    if backtrack(child, i + 1):
                        return True
                return False

            if c not in node.children:
                return False

            return backtrack(node.children[c], i + 1)


        return backtrack(self.root, 0)

