class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def brute(l, r):
            if l == r:
                return True

            if l + 1 == r:
                return s[l] == s[r]

            return s[l] == s[r] and brute(l + 1 , r - 1)

        cache = {}
        def memo(l, r):
            if l == r:
                cache[(l, r)] = True
                return True
            
            if l + 1 == r:
                cache[(l , r)] = s[l] == s[r]
                return s[l] == s[r]

            cache[(l, r)] = s[l] == s[r] and memo(l + 1, r - 1)
            return cache[(l, r)]


        def dp():
            n = len(s)
            dp = [[False] * n for _ in range(n)]

            for i in range(n):
                dp[i][i] = True

            result = n
            for length in range(2, n + 1):
                for l in range(n - length + 1):
                    r = l + length - 1

                    if s[l] == s[r]:
                        if length == 2:
                            dp[l][r] = True
                            result += 1
                        elif dp[l + 1][r - 1]:
                            dp[l][r] = True
                            result += 1

            return result


        # result = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if memo(i, j):
        #             result += 1

        return dp()