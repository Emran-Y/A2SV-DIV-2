class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # row

        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in row:
                    return False
                if board[i][j] != '.':row.add(board[i][j])
            
        # col

        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in col:
                    return False
                if board[j][i] != '.':col.add(board[j][i])
        
        # partition

        for i in range(9):
            row = set()
            for j in range((i//3) * 3  ,((i//3) * 3) + 3):
                for k in range(3*(i%3),3*(i%3) + 3):
                    if board[j][k] != '.' and board[j][k] in row:
                        return False
                    if board[j][k] != '.':row.add(board[j][k])
        return True
                    
