class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutiveOnes = 0
        maxConsecutiveOnes = 0

        for num in nums:
            consecutiveOnes = consecutiveOnes + 1 if num else 0
            maxConsecutiveOnes = max(maxConsecutiveOnes, consecutiveOnes)

        return maxConsecutiveOnes