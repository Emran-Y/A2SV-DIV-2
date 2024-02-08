class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] * nums[i])
        
        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]

        for i in range(len(nums) - 2 , -1 , -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        for i in range(len(nums)):
            if(i - 1 >= 0 and i + 1 < len(nums)):
                nums[i] = prefix[i-1] * suffix[i+1]
            elif(i - 1 >= 0):
                nums[i] = prefix[i-1]
            elif(i+1<len(nums)):
                nums[i] = suffix[i+1]
        return nums



        