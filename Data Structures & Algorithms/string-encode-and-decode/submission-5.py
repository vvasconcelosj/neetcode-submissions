class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            encoded = str(len(s)) + "#" + s
            result += encoded
        return result

    def decode(self, s: str) -> List[str]:

        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i: j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result

