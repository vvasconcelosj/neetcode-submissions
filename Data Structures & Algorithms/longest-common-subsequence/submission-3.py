class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def brute(i, j):
            if i == len(text1):
                return 0

            if j == len(text2):
                return 0


            if text1[i] == text2[j]:
                return 1 + brute(i + 1, j + 1)

            return max(brute(i + 1, j), brute(i, j + 1))

        cache = {}
        def memo(i, j):
            if i == len(text1):
                return 0

            if j == len(text2):
                return 0


            if (i, j) in cache:
                return cache[(i, j)]


            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + memo(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = max(memo(i + 1, j), memo(i, j + 1))
            return cache[(i, j)]

        return memo(0, 0)


        def dp():
            n = len(text1)
            m = len(text2)
            dp = [[0] * (m + 1) for _ in range(n + 1)]

            for i in range(n - 1, -1, -1):
                for j in range(m - 1, -1, -1):
                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

            return dp[0][0]

        return dp()