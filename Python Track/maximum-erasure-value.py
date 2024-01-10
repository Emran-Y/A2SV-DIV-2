class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        

        window = {}
        max_ = 0
        sum_ = 0
        sum_l = 0
        
        l = 0

        for R in range(len(nums)):
            window[nums[R]] = 1 + window.get(nums[R],0)
            sum_+=nums[R]
            sum_l+=1


            while(sum_l > len(window)):
                window[nums[l]]-=1
                sum_-=nums[l]
                sum_l-=1
                if(window[nums[l]] == 0):
                    del window[nums[l]]
                l+=1
                
            max_ = max(max_,sum_)
        return max_