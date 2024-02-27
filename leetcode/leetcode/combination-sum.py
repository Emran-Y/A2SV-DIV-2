class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(idx,cur,tot):
            if tot == target:
                ans.append(cur[:])
                return
            if tot > target or idx >= len(candidates):
                return
            cur.append(candidates[idx])
            backtrack(idx,cur,tot + candidates[idx])
            cur.pop()
            backtrack(idx+1,cur,tot)
        backtrack(0,[],0)
        return ans
            
            