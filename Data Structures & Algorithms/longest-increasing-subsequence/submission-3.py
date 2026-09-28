class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def brute(i, prev):
            if i == len(nums):
                return 0

            skip = brute(i + 1, prev)
            include = 0
            if nums[i] > prev:
                include = 1 + brute(i + 1, nums[i])

            return max(skip, include)


        cache = {}
        def memo(i, prev):
            if i == len(nums):
                return 0

            skip = memo(i + 1, prev)
            include = 0
            if nums[i] > prev:
                include = 1 + memo(i + 1, nums[i])

            cache[i] = max(skip, include)

            return cache[i]

        def dp():
            n = len(nums)
            dp = [1] * len(nums)

            for i in range(len(nums) - 1, -1, -1):
                for j in range(i + 1, len(nums)):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[i], 1 + dp[j])
              
            return max(dp)

        
        return dp()

