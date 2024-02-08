class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)
        
        tot = sum(nums)
        for i in range(1,len(prefix_sum)):
            if(prefix_sum[i - 1] == tot - prefix_sum[i]):
                return i - 1
        return -1