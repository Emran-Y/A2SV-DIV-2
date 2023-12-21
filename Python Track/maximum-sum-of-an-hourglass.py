class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        _max = 0

        for i in range(len(grid)):
            if(len(grid) - i >= 3):

                for j in range(len(grid[0])):
                    if(len(grid[0]) - j >= 3):
                        _max = max((grid[i][j] + grid[i][j+1] + grid[i][j+2]) + grid[i+1][j+1] +(grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]),_max) 
                    else:
                        break


            else:
                break
        return _max