class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.word_idx = -1

    def has(self, c):
        return c in self.children

    def add_child(self, c):
        if self.has(c):
            return self.children[c]

        self.children[c] = TrieNode()

        return self.children[c]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, idx):
        curr = self.root
        for c in word:
            curr = curr.add_child(c)
            
        curr.word = True
        curr.word_idx = idx




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = Trie()
        for i, word in enumerate(words):
            trie.add(word, i)

        result = []
        
        def backtrack(trie_node, r, c, visited):
            if (
                min(r, c) < 0 or
                r >= len(board) or
                c >= len(board[r]) or
                (r, c) in visited or 
                board[r][c] not in trie_node.children
            ):
                return

            letter = board[r][c]

            visited.add((r, c))

            new_node = trie_node.children[letter]
            
            if new_node.word and new_node.word_idx >= 0:
                result.append(words[new_node.word_idx])
                new_node.word_idx = -1
        
            backtrack(new_node, r + 1, c, visited)
            backtrack(new_node, r - 1, c, visited)
            backtrack(new_node, r, c + 1, visited)
            backtrack(new_node, r, c - 1, visited)

            visited.remove((r, c))
            

        for r in range(len(board)):
            for c in range(len(board[r])):
                backtrack(trie.root, r, c, set())

        return result

            