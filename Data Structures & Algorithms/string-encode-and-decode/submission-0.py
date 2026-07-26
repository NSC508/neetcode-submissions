class Solution:

    def encode(self, strs: List[str]) -> str:
        # what we can do is have something like a delimiter at the end 
        str = ""
        for index, value in enumerate(strs):
            str += f'{len(value)}#{value}'
        return str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
