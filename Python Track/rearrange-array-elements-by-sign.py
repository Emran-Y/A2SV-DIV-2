class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        arr_p = []
        arr_n = []

        for i in nums:
            if(i > 0 ):
                arr_p.append(i)
            else:
                arr_n.append(i)

        L = 0

        final = []

        while(L < len(arr_n)):
            final.append(arr_p[L])
            final.append(arr_n[L])
            L+=1
        return final