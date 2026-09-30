class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            top = result.pop()
            curr = intervals[i]

            # Overlap
            if curr[0] <= top[1]:
                top[1] = max(top[1], curr[1])
                result.append(top)
            else:
                result.append(top)
                result.append(curr)

        return result


        