class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        def brute(i, curr_min, curr_max):

            if i >= len(nums):
                return max(curr_min, curr_max)


            n = nums[i]
            
            tmp = curr_min
            curr_min = min(n * curr_max, n * curr_min, n)
            curr_max = max(n * curr_max, n * tmp, n)


            return max(curr_min, curr_max, brute(i + 1, curr_min, curr_max))


        cache = {}
        def memo(i, curr_min, curr_max):

            if i >= len(nums):
                cache[i] = max(curr_min, curr_max)
                return max(curr_min, curr_max)


            if i in cache:
                return cache[i]

            n = nums[i]
            
            tmp = curr_min
            curr_min = min(n * curr_max, n * curr_min, n)
            curr_max = max(n * curr_max, n * tmp, n)

            cache[i] = max(curr_min, curr_max, memo(i + 1, curr_min, curr_max))

            return cache[i]

        def dp():
            n = len(nums)
            dp = [[0, 0] for _ in range(n)]

            dp[0][0] = nums[0]
            dp[0][1] = nums[0]

            res = nums[0]

            for i in range(1, n):
                dp[i][0] = min(nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1], nums[i])
                dp[i][1] = max(nums[i] * dp[i - 1][0], nums[i] * dp[i - 1][1], nums[i])

                res = max(res, dp[i][1])

            return res

        return dp()

