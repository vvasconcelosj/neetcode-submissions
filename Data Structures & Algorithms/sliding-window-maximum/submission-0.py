class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l , r = 0 , 0

        queue = deque()

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                l += 1
                result.append(nums[queue[0]])

            r += 1

        return result


            