class Solution:
    def longestPalindrome(self, s: str) -> str:
        def brute(l, r):
            if l == r:
                return True

            if l + 1 == r:
                return s[l] == s[r]

            return s[l] == s[r] and brute(l + 1, r - 1)

        cache = {}
        def memo(l, r):

            if (l, r) in cache:
             return cache[(l, r)]

            if l == r:
                return True

            if l + 1 == r:
                return s[l] == s[r]

            cache[(l, r)] = s[l] == s[r] and memo(l + 1, r - 1)

            return cache[(l , r)]

        # longest = float('-inf')
        # longest_idx = (0, 0)
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if memo(i, j) and (j - i + 1) > longest:
        #             longest = j - i + 1
        #             longest_idx = (i, j)

        # return s[longest_idx[0]:longest_idx[1] + 1]

        def dp():
            n = len(s)
            dp = [[False] * n for _ in range(n)]

            for i in range(n):
                dp[i][i] = True

            start , max_len = 0, 1
            for length in range(2, n + 1):
                for l in range(n - length  + 1):
                    r = l + length - 1
                    if s[l] == s[r]:
                        if length == 2:
                            dp[l][r] = True
                        elif dp[l + 1][r - 1]:
                            dp[l][r] = True

                        if dp[l][r] and length > max_len:
                            start, max_len = l , length
            return s[start:start + max_len]

        return dp()
        

                    
