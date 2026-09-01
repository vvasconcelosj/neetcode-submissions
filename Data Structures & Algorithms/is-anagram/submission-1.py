class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = {}

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1


        for c in t:
            if c in s_map:
                if s_map[c] > 0:
                    s_map[c] -= 1
                    if s_map[c] == 0:
                        del s_map[c]
                else:
                    return False
            else:
                return False

        return True if not s_map else False