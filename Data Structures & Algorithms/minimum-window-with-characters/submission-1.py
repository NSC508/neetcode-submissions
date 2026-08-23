class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def meetsReq(s_freq, t_freq):
            for index, value in enumerate(s_freq):
                if value < t_freq[index]:
                    return False
            return True

        if len(t) > len(s):
            return ""
        t_freq = [0] * 52
        for char in t:
            if ord(char) >= 97:
                t_freq[ord(char) - ord('a') + 26] += 1
            else:
                t_freq[ord(char) - ord('A')] += 1
        
        l = 0
        minLen = float('inf')
        minString = ""
        s_freq = [0] * 52
        for r in range(len(s)):
            char = s[r]
            if ord(char) >= 97:
                s_freq[ord(char) - ord('a') + 26] += 1
            else:
                s_freq[ord(char) - ord('A')] += 1
            while meetsReq(s_freq, t_freq):
                char = s[l]
                if ord(char) >= 97:
                    s_freq[ord(char) - ord('a') + 26] -= 1
                else:
                    s_freq[ord(char) - ord('A')] -= 1
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minString = s[l:r+1]
                l += 1
        return minString