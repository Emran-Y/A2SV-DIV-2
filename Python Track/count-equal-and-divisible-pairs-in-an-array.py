class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == len(set(nums)):
            return 0
        
        c = 0

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] == nums[j] and i * j % k == 0:
                    c+=1
        return c