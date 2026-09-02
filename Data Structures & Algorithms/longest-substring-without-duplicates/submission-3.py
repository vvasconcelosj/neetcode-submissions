class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()

        l = 0 
        result = 0

        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1

            substring.add(s[r])
            result = max(result, len(substring))

        return result