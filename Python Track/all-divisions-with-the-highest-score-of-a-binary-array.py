class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        '''
        nums in the Left contains 0
        nums in the right contains 1

        nums[:i].count(0)
        nums[i:].count(1)

        for 0s

        max become for the last index when i =  len(nums)


        0 0 1 0
                4
        1  2   3 

        4:

        3 -> 
        2 -> 

        '''

        zeros = {len(nums):nums.count(0)}

        m = nums.count(0)
        z = len(nums) - 1
        for i in range(len(nums) - 1,-1,-1):
            if(nums[i] == 0):
                m-=1
                zeros[z] = m
            else:
                zeros[z] = m
            z-=1
        

        ones = {0:nums.count(1)}

        o = 1
        mm = nums.count(1)

        for i in range(len(nums)):
            if(nums[i] == 1):
                mm-=1
                ones[o] = mm
            else:
                ones[o] = mm
            o+=1
        
        ans = []

        maxi = 0

        for i in range(len(nums) + 1):
            maxi = max(maxi,zeros[i] + ones[i])
        
        for i in range(len(nums) + 1):
            if zeros[i] + ones[i] == maxi:
                ans.append(i)
        return ans




