class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        table = {}
        count = 0
        tot_unique = len(set(nums))
        left = 0
        for i in range(len(nums)):
            table[nums[i]] = 1 + table.get(nums[i],0)
            while len(table) == tot_unique and left < len(nums):
                table[nums[left]]-=1
                if table[nums[left]] == 0:
                    del table[nums[left]]
                left+=1
                count+= len(nums) - i
        return count