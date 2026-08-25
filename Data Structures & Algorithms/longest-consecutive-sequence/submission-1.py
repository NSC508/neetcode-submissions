class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinctNums = set(nums)
        longest = 0
        for index, value in enumerate(nums):
            if value - 1 not in distinctNums:
                longestFromIndex = 1
                while value + 1 in distinctNums:
                    longestFromIndex += 1
                    value += 1
                longest = max(longest, longestFromIndex)
        return longest