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

        return memo(0, 0)
        