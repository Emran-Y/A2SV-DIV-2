class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums) == 1):
            return 
        l = 0
        r = 0
        for i in range(len(nums)):
            if(r >= len(nums)):
                return
            else:
                if(nums[l] == 0 and nums[r]!=0):
                    nums[l],nums[r] = nums[r],nums[l]
                    l+=1
                    r+=1
                elif(nums[l]!=0):
                    l+=1
                    r+=1
                elif(nums[l]==0 and nums[r]==0):
                    r+=1
                
            
