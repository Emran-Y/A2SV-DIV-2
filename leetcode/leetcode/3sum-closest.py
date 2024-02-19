class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            
            while L < R:
                temp = nums[i] + nums[L] + nums[R]
                if temp == target:
                    return target
                if ( abs(target - temp) < abs(target - ans) ):
                    ans = temp
                if temp < target:
                    L+=1
                else:
                    R-=1
        return ans