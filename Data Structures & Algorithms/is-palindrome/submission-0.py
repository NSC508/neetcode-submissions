class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            # Move the left pointer if it's not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # Move the right pointer if it's not alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1
                
            # Compare the characters
            if s[l].lower() != s[r].lower():
                return False
                
            # Move both inward for the next check
            l += 1
            r -= 1
            
        return True