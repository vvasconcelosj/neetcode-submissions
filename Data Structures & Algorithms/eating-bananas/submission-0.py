class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:

            rate = left + (right - left) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)

            if time <= h:
                right = rate
            else:
                left = rate + 1
                

        return left