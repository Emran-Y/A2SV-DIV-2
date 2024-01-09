class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        R = 0
        mini = len(nums) + 1
        sum = 0
        while(R < len(nums)):
            sum+=nums[R]
            while(sum >= target):
                    
                    mini = min(mini,R - L + 1)
                    sum-=nums[L]
                    L+=1
            R+=1
        return 0 if mini == len(nums) + 1 else mini
            