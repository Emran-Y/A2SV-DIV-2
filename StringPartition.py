class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # We first build a hash tabel to map the last index of each character

        lasts = {}

        for i,c in enumerate(s):
            lasts[c] = i
        output= []
        size,end = 0,0
        for i,c in enumerate(s):
            size+=1 
            end = max(end,lasts[c])
            if i == end:
                output.append(size)
                size=0
        return output

                
        
