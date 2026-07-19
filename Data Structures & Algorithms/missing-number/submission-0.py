class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # what n is 
        n = len(nums)

        # what the sum should be
        idealSum = sum(range(n + 1))

        # what the actual sum is 
        actualSum = sum(nums)

        # whats the difference
        return idealSum - actualSum