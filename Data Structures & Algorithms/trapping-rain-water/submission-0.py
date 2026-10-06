class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        max_left = [0] * len(height)
        max_right = [0] * len(height)

        curr = height[0]
        for i in range(len(height)):
            curr = max(curr, height[i])
            max_left[i] = curr

        curr = height[-1]
        for i in range(len(height) - 1, -1, -1):
            curr = max(curr, height[i])
            max_right[i] = curr



        water = 0
        for i in range(1, len(height) - 1):

            left = max_left[i]

            right = max_right[i]

            water += min(left, right) - height[i]


        return water