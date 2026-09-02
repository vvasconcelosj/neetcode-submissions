class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_freq = 0
        freq = [0] * 26
        left = 0
        result = 0
        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            freq[index] += 1
            max_freq = max(freq)

            while (right - left + 1) - max_freq > k:
                index = ord(s[left]) - ord('A')
                freq[index] -= 1
                left += 1

            result = max(result, right - left + 1)


        return result
