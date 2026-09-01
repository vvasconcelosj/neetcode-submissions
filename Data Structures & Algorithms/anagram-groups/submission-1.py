class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            s_sorted = "".join(sorted(s))
            
            if s_sorted in groups:
                groups[s_sorted].append(s)
            else:
                groups[s_sorted] = [s]

        result = []
        for group in groups:
            partial = []
            for s in groups[group]:
                partial.append(s)
            result.append(partial)

        return result