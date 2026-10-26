class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dst, time in times:
            adj[src].append((dst, time))

        shortest = {}
        min_heap = [(0, k)]

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            if node in shortest:
                continue

            shortest[node] = dist
            for neighbor, time in adj[node]:
                if neighbor not in shortest:
                    heapq.heappush(min_heap, (time + dist, neighbor))

        min_time = -1
        for i in range(1, n + 1):
            if i in shortest:
                min_time = max(min_time, shortest[i])
            else:
                return -1

        return min_time