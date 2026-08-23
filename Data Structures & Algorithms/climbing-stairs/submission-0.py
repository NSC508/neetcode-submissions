class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(needed):
            if needed == 0:
                return 1
            if needed < 0:
                return 0
            if needed in dp:
                return dp[needed]
            ways = dfs(needed - 1) + dfs(needed - 2)
            dp[needed] = ways
            return ways
        return dfs(n)