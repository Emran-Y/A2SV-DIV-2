class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i] = 0
            else:
                nums[i] = 1
        ans = 0
        feq = {}
        res = 0

        right = 0

        while right < len(nums):
            res+=nums[right]
            if res == k:
                ans+=1
            
            ans+=feq[res-k] if res-k in feq else 0
            feq[res] = feq.get(res,0) + 1
            right+=1

        return ans

