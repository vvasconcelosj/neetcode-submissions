class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = { node: [] for node in range(n)}

        visited = set()

        def traverse(node):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adjacency_list[node]:
                traverse(neighbor)

            return True


        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        result = 0
        for node in range(n):
            if traverse(node):
                result += 1

        return result
        