class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        if(tot%p==0):
            return 0
        if(tot < p):
            return -1
        table = {0:-1}


        sum_ = 0
        idx = inf
        target = tot%p

        for i in range(len(nums)):
            sum_ += nums[i]

            if (sum_%p - target )%p in table:
                idx = min(idx,i-table[(sum_%p - target)%p])
            table[sum_%p] = i
        return idx if idx!=inf and idx < len(nums) else -1