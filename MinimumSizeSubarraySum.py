class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        L = 0
        R = 0
        mini = 0
        while(R < len(nums)):
            if(sum < target):
                sum+=nums[R]
               
                R+=1
            else:
                if(mini == 0):
                    mini = R - L
                else:
                    mini = min(mini,R - L)
                sum-=nums[L]
                L+=1
        while(sum >= target):
            if(mini == 0):
                    mini = R - L
            else:
                mini = min(mini,R - L)
            sum-=nums[L]
            L+=1
        return mini
