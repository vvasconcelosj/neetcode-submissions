class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # max_left = [0] * len(height)
        # max_right = [0] * len(height)

        # curr = height[0]
        # for i in range(len(height)):
        #     curr = max(curr, height[i])
        #     max_left[i] = curr

        # curr = height[-1]
        # for i in range(len(height) - 1, -1, -1):
        #     curr = max(curr, height[i])
        #     max_right[i] = curr



        # water = 0
        # for i in range(1, len(height) - 1):

        #     left = max_left[i]

        #     right = max_right[i]

        #     water += min(left, right) - height[i]


        # return water

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water