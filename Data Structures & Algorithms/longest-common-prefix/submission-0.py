class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        ptr = 0
        minLength = min(len(s) for s in strs)
        while ptr < minLength:
            letter = strs[0][ptr]
            for i in range(len(strs)):
                if strs[i][ptr] != letter:
                    return ret
            ret += letter
            ptr += 1
        return ret
