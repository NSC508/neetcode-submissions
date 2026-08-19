class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}
        trusted = {}

        for pair in trust:
            trustee = pair[1]
            truster = pair[0]
            if trustee not in trusted:
                trusted[trustee] = 1
            else:
                trusted[trustee] += 1
            
            if truster not in trusts:
                trusts[truster] = 1
            else:
                trusts[truster] += 1
        
        for index, value in trusted.items():
            if value == n - 1:
                if index not in trusts:
                    return index
        return -1