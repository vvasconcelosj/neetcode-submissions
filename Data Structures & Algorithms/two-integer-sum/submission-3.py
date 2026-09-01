class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev_map = {}

        for i , n in enumerate(nums):
            to_target = target - n

            if to_target in prev_map:
                return [prev_map[to_target], i]
            
            prev_map[n] = i

        return []