class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
            
        freqs = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            freqs[value].append(key)
        
        res = []
        counter = 0
        for i in freqs[::-1]:
            if i != []:
                res.extend(i)
            if len(res) == k:
                return res