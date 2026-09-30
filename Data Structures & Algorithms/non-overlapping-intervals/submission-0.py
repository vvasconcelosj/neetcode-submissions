class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])

        result = [intervals[0]]
        removals = 0
        for start, end in intervals[1:]:
            _, last_end = result[-1]

            # Overlapping
            if start < last_end:
                removals += 1

                if end < last_end:
                    result[-1] = [start, end]

            else:
                result.append([start, end])

        return removals
