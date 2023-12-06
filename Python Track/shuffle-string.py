class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        E = ['r'] * len(s)
        for i in range(len(s)):
            r = indices[i]
            E[r] = s[i]
        return ''.join(E)