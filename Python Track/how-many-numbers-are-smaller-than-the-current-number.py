class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = [0] * len(nums)
        for j in range(len(nums)):
            for i in range(len(nums)):
                if(nums[j] > nums[i]):
                    num[j]+=1
                
        return num
