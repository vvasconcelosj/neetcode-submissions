class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = float("-inf")

        curr = 0

        for i in range(len(nums)):
            curr = max(curr + nums[i], nums[i])

            result = max(result, curr)

        return result