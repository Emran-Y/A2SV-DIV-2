class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [nums[0]]
        cur = nums[0]
        for i in range(1,len(nums)):
            cur+=nums[i]
            arr.append(cur)
        return arr