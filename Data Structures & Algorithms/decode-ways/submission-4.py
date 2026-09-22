class Solution:
    def numDecodings(self, s: str) -> int:
        
        def brute(i):
            if i >= len(s):
                return 1

            if s[i] == "0":
                return 0

            result = brute(i + 1)
            if s[i] == "1" or (
                s[i] == "2" and i + 1 < len(s) and int(s[i + 1]) <= 6
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
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and int(s[i+1]) <= 6)):
                result += memo(i + 2)

            cache[i] = result

            return cache[i]



        return memo(0)