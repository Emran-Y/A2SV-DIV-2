class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0
        R = len(nums) - 1

        while(R > L):
            if nums[L] == val and nums[R] != val:
                nums[L],nums[R] = nums[R],nums[L]
                L+=1
                R-=1
            elif nums[L] == val and nums[R] == val:
                R-=1
            elif nums[L] != val and nums[R] != val:
                L+=1
            elif nums[L] != val and nums[R] == val:
                R-=1
                L+=1
        return len(nums) - nums.count(val)


            