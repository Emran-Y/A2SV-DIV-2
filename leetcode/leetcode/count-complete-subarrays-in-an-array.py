class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0
        tot = len(set(nums))
        for i in range(len(nums)):
            temp = {nums[i]}
            if len(temp) == tot:
                count+=1
            for i in range(i+1,len(nums)):
                temp.add(nums[i])
                if len(temp) == tot:
                    count+=1
                

        return count