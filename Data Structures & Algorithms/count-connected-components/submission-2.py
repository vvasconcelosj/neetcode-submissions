class UnionFind:
    def __init__(self, n):
        self.parent = { i:i for i in range(n) }
        self.rank = { i: 0 for i in range(n) }

    def find(self, n):
        parent = self.parent[n]

        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent

    def union(self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        
        # self parent
        if parent_a == parent_b:
            return False

        if self.rank[parent_b] > self.rank[parent_a]:
            parent_a, parent_b = parent_b, parent_a

        self.parent[parent_b] = parent_a
        self.rank[parent_a] += 1

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        result = n
        for a, b in edges:
            if uf.union(a, b):
                result -= 1

        return result
        