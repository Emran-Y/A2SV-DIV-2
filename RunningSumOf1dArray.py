class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num =  [ ]

        for i in range(len(nums)):
            if(i==0):
                num.append(nums[i])
            else:
                num.append(num[i - 1] + nums[i])
        return num
