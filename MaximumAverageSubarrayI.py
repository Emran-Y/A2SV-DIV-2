class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L = 0
        maxi = 0
        sum = 0
        for i in range(len(nums)):
            if(i + 1 - L >= k):
                sum+=nums[i]
                if(maxi != 0):
                    maxi = max(sum/k,maxi)
                else:
                    maxi = sum/k
                sum-=nums[L]
                L+=1
            else:
                sum+=nums[i]
        return maxi
