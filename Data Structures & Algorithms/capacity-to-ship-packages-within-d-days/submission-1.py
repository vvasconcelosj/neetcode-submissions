class Solution:
    def can_ship(self, cap, days, weights):
        days_used = 1
        space_left = cap
        for weight in weights:
            if space_left - weight < 0:
                days_used += 1
                space_left = cap

            space_left -= weight

        return days_used <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left, right = max(weights), sum(weights)

        while left < right:

            mid = left + (right - left) // 2

            # We can ship in less than days, let's try shorter but mid maybe our answer
            if self.can_ship(mid, days, weights):
                right = mid
            else:
                # We can't ship, try bigger
                left = mid + 1

        return left