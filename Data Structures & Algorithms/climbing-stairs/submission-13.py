class Solution:
    def climbStairs(self, n: int) -> int:

        def brute(n):
            if n == 2:
                return 2
            if n == 1:
                return 1

            return brute(n - 1) + brute(n - 2)

        cache = {}
        # top - bottom
        def memo(n):
            if n == 2:
                return 2
            if n == 1:
                return 1

            if n in cache:
                return cache[n]

            cache[n] =  memo(n - 1) + memo(n - 2)

            return cache[n]

        # bottom - up
        def dp(n):
            if n <= 2:
                return n

            one , two = 1, 2

            for i in range(n - 2):
                one, two = two, one + two


            return two


        return dp(n)
        