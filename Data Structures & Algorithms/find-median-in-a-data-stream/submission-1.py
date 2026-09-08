class MedianFinder:

    def __init__(self):
        self.min_heap = [] # Stores the right side 
        self.max_heap = [] # Stores the left side, data stored as negatives
         

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            self.max_heap.append(num * -1)
            return

        left_boundary = self.max_heap[0] * -1

        if num > left_boundary:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, num * -1)

        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            self.rebalance()
        

    def findMedian(self) -> float:
        
        if abs(len(self.min_heap) - len(self.max_heap)) == 0:
            # Same number of elements we can pick both tops
            left = self.max_heap[0] * -1
            right = self.min_heap[0]

            return (left + right) / 2

        if len(self.min_heap) > len(self.max_heap):
            # Min heap has one more element which is the median
            return self.min_heap[0]
        else:
            return self.max_heap[0] * -1



    def rebalance(self) -> None:
        if len(self.min_heap) > len(self.max_heap):
            # Min heap has more elements 
            top = self.min_heap[0]

            while self.min_heap and self.min_heap[0] == top:
                num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, num * -1)

        else:
            # Max heap has more elements
            top = self.max_heap[0]

            while self.max_heap and self.max_heap[0] == top:
                num = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, num * -1)