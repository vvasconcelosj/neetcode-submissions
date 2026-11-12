class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[right] + numbers[left]

            if curr_sum == target:
                return [left + 1, right + 1]

            if curr_sum > target:
                right -= 1
            else:
                left += 1
        return []