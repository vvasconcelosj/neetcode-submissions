class Solution:
    def char_to_int_index(self, c: str):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            return 26 + ord(c) - ord('a')
        return ord(c) - ord('A')

    def has_same_freq(self, freq: list[int], compare_to: list[int] ):
        for i in range(26 * 2):
            if compare_to[i] < freq[i]:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        
        # Build t_freq to lookup for same letters
        t_freq = [0] * (26 * 2)
        for c in t:
            index = self.char_to_int_index(c)
            t_freq[index] += 1

        # print(t_freq)
        left = 0
        substring_freq = [0] *  (26 * 2)
        substring = ''
        min_length = float('inf')
        min_substring = ''
        for right in range(len(s)):
            index = self.char_to_int_index(s[right])
            substring_freq[index] += 1
            substring += s[right]
            # print(substring, substring_freq)

            while self.has_same_freq(t_freq, substring_freq):
                if len(substring) < min_length:
                    min_length = len(substring)
                    min_substring = substring

                index = self.char_to_int_index(s[left])
                substring_freq[index] -= 1
                left += 1
                substring = substring[1:]

          


        return min_substring

