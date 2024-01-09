class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        d = {0:0,1:0}

        l = 0
        ans = 0

        for R in range(len(nums)):
            d[nums[R]]+=1

            while(d[0] > 1):
                d[nums[l]]-=1
                l+=1
            ans = max(ans,sum(d.values()) - 1)

        return ans
            


    
    
   
        
                    
            