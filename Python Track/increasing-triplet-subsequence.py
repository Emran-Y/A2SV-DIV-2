class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min_ = []
        for i in nums:
            if len(min_) == 0:
                min_.append(i)
                continue
            if(min_[-1] > i):
                min_.append(i)
            else:
                min_.append(min_[-1])

        max_ = []

        for i in range(len(nums) - 1, -1, -1):
            if len(max_) == 0:
                max_.append(nums[i])
            else:
                if nums[i] > max_[-1]:
                    max_.append(nums[i])
                else:
                    max_.append(max_[-1])

        max_ = max_[::-1]  


        


        for i in range(len(nums)):
            if(i==0):
                continue
            if(i==len(nums) - 1):
                continue
            if(min_[i-1] < nums[i] and nums[i] < max_[i+1] ):
                return True
        return False
      


        

                    
                