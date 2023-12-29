class Solution:
    def sortSentence(self, s: str) -> str:
        

        org = s.split()
        store = {}
        for i in org:
            idx = i[-1]
            val = i[:-1]
            store[int(idx)] = val
        
        res = "" 
        for i in range(len(org)):
            res += store[i+1]
            res += " "
        return res[:-1]