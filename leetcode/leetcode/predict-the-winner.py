class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visited = defaultdict(int)
        def winner(left,right,turn):
            if left > right:
                return 0
            if (left,right,turn) in visited:
                return visited[(left,right,turn)]
            res = 0

            if turn == 1:
                res = max(nums[left] + winner(left+1,right,2),nums[right] + winner(left,right-1,2))
            else:
                res = min(winner(left + 1,right,1),winner(left,right-1,1))
            visited[(left,right,turn)] = res
            return res
        p1 = winner(0,len(nums) - 1,1)

        return sum(nums) - p1 <= p1