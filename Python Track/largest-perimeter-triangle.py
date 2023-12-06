class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        maxi = 0
        L = len(nums) - 3
        R = len(nums) - 1

        while(L > -1):
            if(nums[L] + nums[L+1] <= nums[R]):
                R-=1
                L-=1
            else:
                maxi = max(maxi,nums[L] + nums[L+1] + nums[L+2])
                L-=1
                R-=1
        return maxi