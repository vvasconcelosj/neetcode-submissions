class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i


        for i, n in enumerate(nums):
            to_target = target - n
            if to_target in indices and indices[to_target] != i:
                return [i, indices[to_target]]

        return []