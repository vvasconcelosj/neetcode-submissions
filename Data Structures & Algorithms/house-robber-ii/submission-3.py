class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def brute(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            return max(
                brute(i + 1, flag),
                nums[i] + brute(i + 2, flag)
            )

        cache = {}
        def memo(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0

            if i in cache:
                return cache[i]

            cache[i] = max(
                brute(i + 1, flag),
                nums[i] + brute(i + 2, flag)
            )

            return cache[i]


        def dp(nums):
            if len(nums) == 1:
                return nums[0]
                
            dp = [0] * len(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(
                    dp[i - 1],
                    nums[i] + dp[i - 2]
                )

            return dp[-1]

        return max(
            dp(nums[1:]),
            dp(nums[:-1])
        )