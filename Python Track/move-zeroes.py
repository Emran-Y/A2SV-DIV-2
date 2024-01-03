class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return None
        L = 0
        R = 1

        while(R < len(nums)):
            if (nums[R] != 0 and nums[L] != 0):
                R+=1
                L+=1
            elif(nums[L] != 0 and nums[R]==0):
                R+=1
                L+=1
            elif(nums[L]==0 and nums[R]!=0):
                nums[L],nums[R] = nums[R],nums[L]
                R+=1
                L+=1
            elif(nums[L] == 0 and nums[R] == 0):
                R+=1
        