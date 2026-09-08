class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(i, curr_sum, curr):
            if i >= len(nums):
                return []

            if curr_sum > target:
                return []

            if curr_sum == target:
                result.append(curr.copy())
                return curr

            curr.append(nums[i])
            backtrack(i, curr_sum + nums[i], curr)
            curr.pop()
            backtrack(i + 1, curr_sum, curr)

            return curr
        
        backtrack(0, 0, [])
        return result