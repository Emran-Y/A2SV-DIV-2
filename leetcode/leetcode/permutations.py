class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(cur,vis):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            for i in range(len(nums)):
                if nums[i] not in vis:
                    cur.append(nums[i])
                    vis.add(nums[i])
                    helper(cur,vis)
                    cur.pop()
                    vis.remove(nums[i])
        helper([],set())
        return ans

