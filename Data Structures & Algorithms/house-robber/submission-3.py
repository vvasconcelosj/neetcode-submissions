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


        def dp():
            if len(nums) == 1:
                return nums[0]
                
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

            return dp[-1]


        return dp()

