class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

            
        s_map = {}

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1


        for c in t:
            if c not in s_map or s_map[c] <= 0:
                return False

            s_map[c] -= 1

        return True