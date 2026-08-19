class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = 0
        l = 0
        r = 0
        while r < l + k:
            if blocks[r] == "W":
                whiteCount += 1
            r += 1
        minSwap = whiteCount
        for r in range(r, len(blocks)):
            if blocks[r] == "W":
                whiteCount += 1
            if blocks[l] == "W":
                whiteCount -= 1
            l += 1
            minSwap = min(minSwap, whiteCount)
        return minSwap