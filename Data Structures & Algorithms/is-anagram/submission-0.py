class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sFreq = [0] * 26
        tFreq = [0] * 26
        for i in range(len(s)):
            sFreq[ord(s[i]) - ord('a')] += 1
            tFreq[ord(t[i]) - ord('a')] += 1
        return sFreq == tFreq
            