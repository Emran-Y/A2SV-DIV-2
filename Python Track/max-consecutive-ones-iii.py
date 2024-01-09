class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        

        ans = 0

        d = {0:0,1:0}

        l = 0

        for R in range(len(nums)):
            d[nums[R]]+=1

            while(d[0] > k):
                d[nums[l]]-=1
                l+=1
            ans = max(ans,sum(d.values()))
        return ans