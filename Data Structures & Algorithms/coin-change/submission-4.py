class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def brute(remaining):
            if remaining == 0:
                return 0

            best = float('inf')
            for coin in coins:
                if remaining - coin >= 0:
                    best = min(best, 1 + brute(remaining - coin))

            return best

        # res = brute(amount)

        # return res if res != float('inf') else -1


        def dp():
            dp = [float('inf')] * (amount + 1)
            dp[0] = 0

            for a in range(amount + 1):
                for coin in coins:
                    if a - coin >= 0:
                        dp[a] = min(dp[a], dp[a - coin] + 1)

            return dp[amount]


        res = dp()

        return res if res != float('inf') else -1


            