class Solution:
    def dfs(self, src , adj, visited, top_sort, path):
        # Cycle
        if src in path:
            return False

        if src in visited:
            return True

        path.add(src)
        visited.add(src)
        for dst in adj[src]:
            if not self.dfs(dst, adj, visited, top_sort, path):
                return False

        top_sort.append(src)
        path.remove(src)
        return True

    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []

        for src, dst in edges:
            adj[src].append(dst)

        top_sort = []
        visited = set()

        for i in range(n):
            if not self.dfs(i, adj, visited, top_sort, set()):
                return []

        top_sort.reverse()

        return top_sort
