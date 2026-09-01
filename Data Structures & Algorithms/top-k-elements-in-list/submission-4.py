class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count numbers frequency
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # use bucket sort to place the elements
        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        # build the top k iterating from right to left
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result

        
