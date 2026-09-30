class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])

        removals = 0
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= last_end:
                last_end = end
            else:
                removals += 1
                last_end = min(end, last_end)

        return removals
