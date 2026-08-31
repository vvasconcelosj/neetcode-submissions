class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        result = [0] * (len(nums) * 2)

        for i in range(len(nums)):
            result[i] = nums[i]
            result[i + len(nums)] = nums[i]

        return result