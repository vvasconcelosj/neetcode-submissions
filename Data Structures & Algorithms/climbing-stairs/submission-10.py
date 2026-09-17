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
            one = 0
            two = 1

            for i in range(n):
                tmp = two 
                two = one + two
                one = tmp

            return two


        return dp(n)
        