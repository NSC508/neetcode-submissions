class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(x):
            if len(x) == 0:
                return True
            if x in dp:
                return dp[x]
            possible = []
            for w in wordDict:
                if x.startswith(w):
                    possible.append(
                        dfs(x[len(w):])
                    )
            if len(possible) == 0:
                return False
            canFind = max(possible)
            dp[x] = canFind
            return canFind
        return dfs(s)
                