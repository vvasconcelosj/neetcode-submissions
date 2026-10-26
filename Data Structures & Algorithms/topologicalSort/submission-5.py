
class Solution:
    def dfs(self, src, adj: dict[str, list[int]], visited: set[int], path: set[int], top_sort: list[int]) -> bool:
        if src in path:
            return False

        if src in visited:
            return True

        visited.add(src)
        path.add(src)

        for dst in adj[src]:
            if not self.dfs(dst, adj, visited, path, top_sort):
                return False

        top_sort.append(src)
        path.remove(src)

        return True

    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)

        for src, dst in edges:
            adj[src].append(dst)

        
        visited = set()
        result = []

        for i in range(n):
            if not self.dfs(i, adj, visited, set(), result):
                return []

        result.reverse()

        return result