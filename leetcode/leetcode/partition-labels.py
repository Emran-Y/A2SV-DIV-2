class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = i
        store = []
        size = 0
        end = 0
        R = 0
        for R in range(len(s)):
            size+=1
            end = max(end,dict[s[R]])
            if (R == end):
                store.append(size)
                size=0
        return store     
