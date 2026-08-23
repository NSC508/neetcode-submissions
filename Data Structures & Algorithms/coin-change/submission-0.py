class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(needed):
            if needed == 0:
                return 0
            if needed < 0:
                return -1
            if needed in dp:
                return dp[needed]
            min_coins = float('inf')
            for coin in coins:
                res = dfs(needed - coin)
                if res != -1:
                    min_coins = min(min_coins, 1 + res)

            dp[needed] = min_coins if min_coins != float('inf') else -1
            return dp[needed]
        return dfs(amount)
            