class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_num_of_moves = 0
        while target > 1 and maxDoubles > 0:
            if target%2 == 0:
                min_num_of_moves+=1
                target = target // 2
                maxDoubles-=1
            else:
                min_num_of_moves+=1
                target-=1
        return min_num_of_moves + (target-1)