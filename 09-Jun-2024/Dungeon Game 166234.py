# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row,col = len(dungeon), len(dungeon[0])
        @cache
        def dp(r, c):
            if r >= row or c >= col:
                return float("inf")
            
            if r == row-1 and c == col - 1:
                return max(-dungeon[r][c], 0)
            
            return max(min(dp(r+1, c), dp(r, c+1)) - dungeon[r][c],0)

        return dp(0, 0) + 1