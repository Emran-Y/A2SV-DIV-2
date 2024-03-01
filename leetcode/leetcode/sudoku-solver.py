class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(r,c,k):
            for i in range(9):
                if board[r][i] == k:
                    return False
                if board[i][c] == k:
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3]==k: 
                    return False
            return True
        def bulder(r,c):
            if r == 9:
                return True
            if c == 9:
                return bulder(r+1,0)
            if board[r][c] == '.':
                for k in range(1,10):
                    if isValid(r,c,str(k)):
                        board[r][c] = str(k)
                        if bulder(r,c+1):
                            return True
                        board[r][c] = '.'
                return False
            return bulder(r,c+1) 
            
        bulder(0,0)
                
