class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = []

        def backtrack(idx,cur):
            if idx >= len(nums):
                powerset.append(cur[:])
                return
            powerset.append(cur[:])
            for i in range(idx,len(nums)):
                cur.append(nums[i])
                backtrack(i+1,cur)
                cur.pop()
        backtrack(0,[])
        return powerset

        