class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        result = []
        for i in range(len(intervals)):
            start , end = newInterval

            curr_start, curr_end = intervals[i]
            # Non overlap on start
            if end < curr_start:
                result.append(newInterval)
                return result + intervals[i:]
            elif start > curr_end:
                result.append(intervals[i])
            else:
                newInterval = [min(start, curr_start), max(end, curr_end)]

        result.append(newInterval)
        return result
            