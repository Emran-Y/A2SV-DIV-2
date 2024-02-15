class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        north = [0] * len(grid)
        east = []
        maximum_total_sum_increased = 0
        for i in range(len(grid)):
            east.append(max(grid[i]))
        for i in range(len(grid)):
            for j in range(len(grid)):
                north[j] = max(north[j],grid[i][j])
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] <  min(east[i],north[j]):
                    maximum_total_sum_increased+=min(east[i],north[j]) - grid[i][j]
        return maximum_total_sum_increased
        
