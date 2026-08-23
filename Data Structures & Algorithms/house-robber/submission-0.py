class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(nums):
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            if tuple(nums) in dp:
                return dp[tuple(nums)]
            take = nums[0] + dfs(nums[2:])
            dont = dfs(nums[1:])
            best = max(take, dont)
            dp[tuple(nums)] = best
            return best
        return dfs(nums)