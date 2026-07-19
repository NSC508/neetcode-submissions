class Solution:
    def isValid(self, s: str) -> bool:
        ends = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        bracks = []
        for i in s:
            if i in ends.keys():
                if len(bracks) == 0:
                    return False
                combo = bracks.pop()
                if combo != ends[i]:
                    return False
            else:
                bracks.append(i)
        if len(bracks) > 0:
            return False
        return True