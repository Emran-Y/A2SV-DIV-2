class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        L = 0
        R = len(nums) // 2

        final = []

        while(L < len(nums) // 2 and R < len(nums)):
            final.append(nums[L])
            final.append(nums[R])
            L+=1
            R+=1
        return final