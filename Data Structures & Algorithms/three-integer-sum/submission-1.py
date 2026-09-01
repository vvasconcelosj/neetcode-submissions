class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                b = nums[left]
                c = nums[right]
                total = a + b + c
                if total == 0:
                    result.append([a, b, c])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    right -= 1
                    left += 1
                elif total > 0:
                    right -= 1
                else: 
                    left += 1

        return result
                