class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate prefix
        prefix = 1
        result = [0] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Calcualte posfix
        posfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= posfix
            posfix *= nums[i]

        return result