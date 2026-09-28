class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def brute(i):
            if i == len(s):
                return True


            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if brute(i + len(word)):
                        return True

            return False

        cache = {}
        def memo(i):
            if i == len(s):
                return True

            if i in cache:
                return cache[i]

            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if memo(i + len(word)):
                        return True
            cache[i] = False
            return False

        # return memo(0)

        def dp():
            n = len(s)
            dp = [False for _ in range(n + 1)]
            dp[-1] = True

            for i in range(len(s) - 1, -1, -1):
                for word in wordDict:
                    if i + len(word) <= n and s[i: i + len(word)] == word:
                        dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break

            return dp[0]

        return dp()







  

