class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = [[0] * 26 for i in strs]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                freqs[i][ord(strs[i][j]) - ord('a')] += 1
        
        groups = {}
        for index, value in enumerate(freqs):
            if tuple(value) not in groups: 
                groups[tuple(value)] = [strs[index]]
            else:
                groups[tuple(value)].append(strs[index])
        
        ret = []
        for key, value in groups.items():
            ret.append(value)

        return ret