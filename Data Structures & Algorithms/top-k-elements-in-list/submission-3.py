class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count numbers frequency
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        # use bucket sort to place the elements
        buckets = [[] for i in range(len(nums) + 1)]
        for num in freqs:
            freq = freqs[num]
            buckets[freq].append(num)

        # build the top k iterating from right to left
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i]:
                continue

            while k > 0 and buckets[i]:
                result.append(buckets[i].pop())
                k -= 1

        return result

        
