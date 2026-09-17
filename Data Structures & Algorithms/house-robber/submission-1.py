class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def brute(i):
            if i >= len(nums):
                return 0

            return max(brute(i + 1), nums[i] + brute(i + 2))

        cache = {}
        def memo(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            cache[i] = max(memo(i + 1), nums[i] + memo(i + 2))
            return cache[i] 

        return memo(0)

