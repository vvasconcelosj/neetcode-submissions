class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1


        have, need = 0, len(t_freq)

        result = (-1, -1)
        result_length = float('inf')
        left= 0

        window = defaultdict(int)
        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in t_freq and window[c] == t_freq[c]:
                have += 1

            while have == need:
                if (right - left+ 1) < result_length:
                    result = (left, right)
                    result_length = right - left+ 1

                window[s[left]] -= 1
                if s[left] in t_freq and window[s[left]] < t_freq[s[left]]:
                    have -= 1

                left += 1

        left, right = result
        return s[left: right + 1] if result_length != float('inf') else ''

        