class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        count = 0

        cur = nums[len(nums) - 1]

        i = len(nums) - 2

        while i > -1:
            temp = math.ceil(nums[i] / cur)
            count+=temp - 1
            cur = math.floor(nums[i] / temp)
                
            i-=1
        return count


