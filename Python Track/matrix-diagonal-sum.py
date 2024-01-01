class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_ = 0
        
        i = 0
        j = 0
        
        while(i < len(mat) and j < len(mat)):
            sum_+=mat[i][j]
            i+=1
            j+=1
        
        i = 0
        j = len(mat) - 1
        
        while(i >= 0 and j >= 0):
            sum_+=mat[i][j]
            i+=1
            j-=1
            
        if (len(mat)%2!=0):
            return sum_ - mat[len(mat) // 2][len(mat) // 2]
        else:
            return sum_