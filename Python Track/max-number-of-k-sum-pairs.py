class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        t = 0
        nums.sort()
        while(r >= 0 and r > l):
            if(nums[r] + nums[l] == k):
                r-=1
                l+=1
                t+=1
            elif(nums[r] + nums[l] > k):
                r-=1
            elif(nums[r] + nums[l] < k):
                l+=1
        return t