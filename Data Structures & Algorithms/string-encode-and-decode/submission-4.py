class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            encoded = str(len(s)) + "#" + s
            result += encoded
        return result

    def decode(self, s: str) -> List[str]:

        i = 0
        length = ''
        result = []
        while i < len(s):
            if s[i] == '#':
                result.append(s[i + 1: i + 1 + int(length)])
                i += int(length)
                length = ''
            else:
                length += s[i]

            i += 1
        return result

