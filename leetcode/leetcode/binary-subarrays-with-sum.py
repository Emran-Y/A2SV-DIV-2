class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p  = {0:1}

        sum_ = 0
        count = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if(sum_ - goal in p):
                count+=p[sum_ -  goal]
            p[sum_] = 1 + p.get(sum_,0)
                
        return count
