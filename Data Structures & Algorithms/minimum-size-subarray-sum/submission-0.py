class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = len(nums) + 1
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minSize = min(minSize, r - l + 1)
                total -= nums[l]
                l += 1
        if minSize == len(nums) + 1:
            return 0
        return minSize