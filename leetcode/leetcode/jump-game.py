class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        cur_target = len(nums) - 1
        from_ = len(nums) - 2
        flag = False
        while from_ >= 0:
            if from_ + nums[from_] >= cur_target:
                cur_target=from_
                from_-=1
                flag = True
            else:
                from_-=1
                flag = False
        return flag 

