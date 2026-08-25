class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # If mid element is greater than rightmost element,
            # the minimum MUST be in the right half (excluding mid).
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is at mid or to its left.
            else:
                r = mid

        return nums[l]