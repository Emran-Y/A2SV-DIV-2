# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, base_str: str) -> str: 
        par = [i for i in range(26)]

        def find(n):
            if par[n] != n:
                par[n] = find(par[n]) 
            return par[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 < p2:
                par[p2] = p1
            else:
                par[p1] = p2
        
        for i in range(len(s1)):
            ch1, ch2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            union(ch1, ch2)

        ans = []
        for w in base_str:
            chr_indx = ord(w) - ord('a')
            ans.append(chr(find(chr_indx) + ord('a')))
        
        return "".join(ans)
