class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        existing = {}

        for i in range(len(nums)):
            existing[nums[i]] = i

        print(existing)
        for i in range(len(nums)):
            to_target = target - nums[i]

            if to_target in existing:
                index = existing[to_target]
                if i != index:
                    return [i, index]

        return null