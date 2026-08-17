class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = result = 0

        for num in nums:
            count = count + 1 if num else 0
            result = max(count, result)

        return result