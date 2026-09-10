class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.word_idx = -1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, idx):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
            
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
                c >= len(board[r])
            ):
                return

            if (r, c) in visited:
                return

            letter = board[r][c]

            if letter not in trie_node.children:
                return

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

            