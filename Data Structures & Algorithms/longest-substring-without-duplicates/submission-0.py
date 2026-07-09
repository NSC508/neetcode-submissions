class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longestSoFar = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            seen.add(s[r])
            longestSoFar = max(longestSoFar, r - l + 1)
        return longestSoFar