class Solution:
    def can_ship(self, capacity: int, weights: list[int], days: int) -> bool:
        space_left = capacity
        days_passed = 1


        for weight in weights:
            if space_left - weight < 0:
                days_passed += 1
                space_left = capacity
            
            space_left -= weight

        return days_passed <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        result = float('inf')
        while left <= right:
            mid = left + (right - left) // 2

            if self.can_ship(mid, weights, days):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result