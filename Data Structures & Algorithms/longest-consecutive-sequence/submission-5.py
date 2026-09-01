class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Create a unique set of numbers so we can verify if next number exist
        unique = set(nums)

        longest = 0

        for n in unique:
            if (n - 1) not in unique:
                length = 0
                while (n + length) in unique:
                    length += 1
                longest = max(longest, length)
        
        return longest