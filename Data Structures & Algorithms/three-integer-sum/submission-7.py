class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            a = nums[i]

            if i > 0 and nums[i - 1] == a:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                b = nums[left]
                c = nums[right]

                if a + b + c > 0:
                    right -= 1
                elif a + b + c < 0:
                    left += 1
                else:
                    result.append([a, b, c])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
        
        return result