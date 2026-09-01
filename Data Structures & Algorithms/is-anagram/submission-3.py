class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        t_freq = [0] * 26
        for c in t:
            index = ord(c) - ord('a')
            t_freq[index] += 1

        for c in s:
            index = ord(c) - ord('a')
            if t_freq[index] <= 0:
                return False

            t_freq[index] -= 1
            

        return True