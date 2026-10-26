class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        p = self.parent[x]

        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    def union(self, x: int, y: int) -> bool:
        p1, p2 = self.find(x), self.find(y)

        # Already on same group
        if p1 == p2:
            return False


        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p2] += 1

        return True



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for src, dst in edges:
            if not uf.union(src, dst):
                return [src, dst]

        return []
        