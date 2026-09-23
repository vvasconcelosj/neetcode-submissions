class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def brute(remaining):
            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            best = float('inf')
            for coin in coins:
                best = min(best, 1 + brute(remaining - coin))

            return best


        cache = {}
        def memo(remaining):
            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            if remaining in cache:
                return cache[remaining]

            best = float('inf')
            for coin in coins:
                best = min(best, 1 + memo(remaining - coin))

            cache[remaining] = best
            return cache[remaining]
                       
        res = memo(amount)
        return res if res != float('inf') else -1