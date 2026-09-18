class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n

        def brute(r, c):
            if r == ROWS or c == COLS:
                return 0

            if r == ROWS - 1 and c == COLS -1:
                return 1

            return brute(r + 1, c) + brute(r, c + 1)

        cache = {}
        def memo(r, c):
            if r == ROWS or c == COLS:
                return 0

            if r == ROWS - 1 and c == COLS -1:
                return 1

            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = memo(r + 1, c) + memo(r, c + 1)

            return cache[(r, c)]

        def dp():
            dp = [[0 for c in range(COLS)] for r in range(ROWS)]
           
            for c in range(COLS):
                dp[ROWS - 1][c] = 1

            for r in range(ROWS):
                dp[r][COLS - 1] = 1

            for r in range(ROWS - 2, -1, -1):
                for c in range(COLS - 2, -1 , -1):
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

            return dp[0][0]



        return dp()
        