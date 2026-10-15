class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        need = {}
        for c in s1:
            s1_freq[c] += 1

        need = len(s1_freq)
        for i in range(len(s2)):
            s2_freq, curr = defaultdict(int), 0

            for j in range(i, len(s2)):
                c = s2[j]
                s2_freq[c] += 1

                if s1_freq[c] < s2_freq[c]:
                    break

                if s1_freq[c] == s2_freq[c]:
                    curr += 1

                if curr == need:
                    return True

        return False

        