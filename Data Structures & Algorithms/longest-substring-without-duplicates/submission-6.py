class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        substr = set()
        result = 0
        for right in range(len(s)):
            c = s[right]

            while c in substr:
                substr.remove(s[left])
                left += 1

            substr.add(c)

            result = max(result, right - left + 1)

        return result