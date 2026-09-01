class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create prefix product
        prefix = []

        curr = 1
        for n in nums:
            prefix.append(curr)
            curr *= n

        # create sufix product
        sufix = [1] * len(nums)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            sufix[i] = curr
            curr *= nums[i]

        # the result is the mulitplication of prefix * sufix 
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * sufix[i])

        return result