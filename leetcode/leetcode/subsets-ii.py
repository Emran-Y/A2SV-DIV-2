class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(idx,cur):
            if idx >= len(nums):
                ans.append(cur[:])
                return
            ans.append(cur[:])

            visited = set()

            for i in range(idx,len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    cur.append(nums[i])
                    backtrack(i+1,cur)
                    cur.pop()
        backtrack(0,[])
        return ans