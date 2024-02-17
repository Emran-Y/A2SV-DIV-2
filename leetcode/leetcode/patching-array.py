from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0
        run_sum = 0

        if nums[0] != 1:
            run_sum = 1
            count = 1

        i = 0
        while run_sum < n:
            if i < len(nums) and nums[i] <= run_sum + 1:
                run_sum += nums[i]
                i += 1
            else:
                run_sum += run_sum + 1
                count += 1
        
        return count