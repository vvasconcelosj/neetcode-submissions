class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)

        for s, d, w in edges:
            adj[s].append((d, w))


        shortest = {}
        min_heap = [(0, src)]

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if node in shortest:
                continue

            shortest[node] = dist

            for neighbor, neighbor_weight in adj[node]:
                if neighbor not in shortest:
                    heapq.heappush(min_heap, (dist + neighbor_weight, neighbor))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest