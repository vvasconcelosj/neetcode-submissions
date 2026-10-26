class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dst, time in times:
            adj[src].append((dst, time))

        shortest = {}
        min_heap = [(0, k)]
        min_time = -1
        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if node in shortest:
                continue

            shortest[node] = dist
            min_time = max(min_time, dist)
            for neighbor, time in adj[node]:
                if neighbor not in shortest:
                    heapq.heappush(min_heap, (time + dist, neighbor))

        return min_time if len(shortest) == n else -1