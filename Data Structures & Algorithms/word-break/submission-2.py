class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # 1. Build the Trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        n = len(s)
        # dp[i] is True if s[i:] can be segmented
        dp = [False] * (n + 1)
        dp[n] = True  # Base case: empty suffix is valid

        # 2. Iterate backwards from end of string
        for i in range(n - 1, -1, -1):
            node = root
            for j in range(i, n):
                ch = s[j]
                if ch not in node.children:
                    break  # Early exit: prefix does not exist in dictionary
                
                node = node.children[ch]
                if node.is_end and dp[j + 1]:
                    dp[i] = True
                    break  # Valid segmentation found for suffix s[i:]

        return dp[0]