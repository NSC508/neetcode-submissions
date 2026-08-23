class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        dp[(m - 1, n - 1)] = 1
        ROWS, COLS = m, n
        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            right = 0
            down = 0
            if r != ROWS - 1:
                down = dfs(r + 1, c)
            if c != COLS - 1:
                right = dfs(r, c + 1)
            dp[(r, c)] = down + right
            return down + right
        return dfs(0, 0)