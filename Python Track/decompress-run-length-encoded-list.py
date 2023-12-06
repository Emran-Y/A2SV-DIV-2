class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        L = 0
        R = 1
        final = []

        while(R < len(nums)):
            final = final + [nums[R]] * nums[L]
            L+=2
            R+=2

        return final