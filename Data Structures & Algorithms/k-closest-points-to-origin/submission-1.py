class Solution:
    def calculate_dist_to_origin(self, x: int, y: int):
        return pow(
            x ** 2 + y ** 2
        , 1/2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = self.calculate_dist_to_origin(x, y)
            min_heap.append((dist, x, y))

        heapq.heapify(min_heap)

        result = []
        while k:
            dist, x , y = heapq.heappop(min_heap)
            result.append((x, y))
            k -= 1

        return result
