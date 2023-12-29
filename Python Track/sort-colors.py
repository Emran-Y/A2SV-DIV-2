class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a,b,c = nums.count(0),nums.count(1),nums.count(2)
        for i in range(len(nums)):
            if a!=0:
                nums[i] = 0
                a-=1
            elif b!=0:
                nums[i] = 1
                b-=1
            else:
                nums[i] = 2