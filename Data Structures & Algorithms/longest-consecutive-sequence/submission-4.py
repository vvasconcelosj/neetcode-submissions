class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Create a unique set of numbers so we can verify if next number exist
        unique = set(nums)

        result = 0
        for num in unique:
            start_of_sequence = num - 1 not in unique

            if start_of_sequence:
                count = 0
                curr = num
                while curr in unique:
                    count += 1
                    curr += 1

                result = max(result, count)


        return result