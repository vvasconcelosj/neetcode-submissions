class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        result = -1
        while left < right:
            height = min(heights[left], heights[right])
            water = (right - left) * height

            result = max(result, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result
