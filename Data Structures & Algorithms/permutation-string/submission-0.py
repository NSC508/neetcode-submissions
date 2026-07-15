class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        windowSize = len(s1)
        originalFreq = [0] * 26
        windowFreq = [0] * 26
        
        # 1. Build the target frequency map
        for char in s1:
            originalFreq[ord(char) - ord('a')] += 1
            
        # 2. Populate the very first window COMPLETELY
        for i in range(windowSize):
            windowFreq[ord(s2[i]) - ord('a')] += 1
            
        # Check if the first window is a match
        if windowFreq == originalFreq:
            return True
            
        # 3. Slide the window across the rest of s2
        for i in range(windowSize, len(s2)):
            # Add the new character on the right
            windowFreq[ord(s2[i]) - ord('a')] += 1
            
            # Remove the old character that fell off the left
            left_char = s2[i - windowSize]
            windowFreq[ord(left_char) - ord('a')] -= 1
            
            # Check the newly formed window
            if windowFreq == originalFreq:
                return True
                
        return False