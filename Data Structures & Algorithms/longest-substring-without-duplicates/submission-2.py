class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        substring = set()

        left = 0
        right = 0

        longest = 0
        while right < len(s):

            if s[right] in substring:
                while left < right and s[left] != s[right]:
                    substring.remove(s[left])
                    left += 1
                left += 1
            else:
                substring.add(s[right])
                longest = max(longest, len(substring))


            right += 1

        return longest