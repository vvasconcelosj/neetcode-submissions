class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        stairs = [1] * n
        stairs[-2] = 2

        for i in range(len(stairs) - 3, -1, -1):
            stairs[i] = stairs[i + 1] + stairs[i + 2]

        return stairs[0]