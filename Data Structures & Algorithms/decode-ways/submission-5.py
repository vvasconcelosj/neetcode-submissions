class Solution:
    def numDecodings(self, s: str) -> int:
        
        def brute(i):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0

            result = brute(i + 1)
            if s[i] == "1" or (
                s[i] == "2" and i + 1 < len(s) and s[i + 1] <= "6"
            ):
                result += brute(i + 2)

            return result

        cache = {}
        def memo(i):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0

            if i in cache:
                return cache[i]

            result = memo(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):
                result += memo(i + 2)

            cache[i] = result

            return cache[i]

        def dp():
            dp = [0] * (len(s) + 1)
            dp[-1] = 1

            for i in range(len(s) - 1, -1, -1):
                if s[i] == "0":
                    dp[i] = 0
                else:
                    dp[i] = dp[i + 1]
                    if i + 1 < len(s) and (s[i] == "1" or  (s[i] == "2" and s[i + 1] <= "6")):
                        dp[i] += dp[i + 2]


            return dp[0]

        return dp()