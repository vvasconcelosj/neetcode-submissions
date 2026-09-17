class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}
        def brute(n):
            if n == 2:
                return 2
            if n == 1:
                return 1

            if n in cache:
                return cache[n]

            cache[n] =  brute(n - 1) + brute(n - 2)

            return cache[n]

        return brute(n)
        