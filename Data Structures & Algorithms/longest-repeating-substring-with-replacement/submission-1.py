class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        maxLen = 0
        for r in range(len(s)):
            char = ord(s[r]) - ord('A')
            freq[char] += 1

            while sum(freq) - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
