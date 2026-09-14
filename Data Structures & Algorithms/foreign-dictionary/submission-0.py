class Solution:


    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = { c: set() for word in words for c in word }

        visited = {}
        result = []
        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True

            visited[c] = False
            result.append(c)

        for i in range(0, len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ''

            for i in range(min(len(w1), len(w2))):
                if w1[i] == w2[i]:
                    continue

                adj[w1[i]].add(w2[i])
                break

        for c in adj:
            if dfs(c):
                return ''

        result.reverse()

        return ''.join(result)
            

