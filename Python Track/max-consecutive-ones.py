class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0 
        temp = 0
        
        for i in nums:
            if(i == 0):
                maxi = max(temp,maxi)
                temp = 0
            else:
                temp+=1
        return max(maxi,temp)
            
        
        