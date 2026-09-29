class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        result = []
        start , end = newInterval
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            # Non overlap on start
            if end < curr_start:
                result.append([start, end])
                return result + intervals[i:]
            elif start > curr_end:
                result.append([curr_start, curr_end])
            else:
                start = min(start, curr_start)
                end = max(end, curr_end)

        result.append([start, end])
        return result
            