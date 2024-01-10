class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        d = {'W':0,'B':0}

        for i in range(k):
            d[blocks[i]]+=1
        min_ = d['W']

        l = 0

        for i in range(k,len(blocks)):
            d[blocks[l]]-=1
            l+=1
            d[blocks[i]]+=1

            min_ = min(min_,d['W'])
        return min_

        