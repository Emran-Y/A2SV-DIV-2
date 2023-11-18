class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        arr = [-1] * len(nums)

        L = 0
        tot = 0  

        for R in range(len(nums)):
            tot+=nums[R]

            if (((R - L) + 1) == ((2 * k) + 1)):
                arr[ L + ((R - L) // 2)] = tot // ((R - L) + 1)
                tot-=nums[L]
                L+=1
            
        return arr
