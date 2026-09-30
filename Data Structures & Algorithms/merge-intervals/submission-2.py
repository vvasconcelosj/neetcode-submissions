class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        result = [intervals[0]]
        for start, end in intervals:
            _, last_end = result[-1]

            if start <= last_end:
                result[-1][1] = max(end, last_end)
            else:
                result.append([start, end])

        return result
