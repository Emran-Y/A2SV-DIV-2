class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        arr = []

        row = 0
        col = 0

        up = True

        while(row < len(mat) and col < len(mat[0]) ):
            if(up):
                while(row>0 and col<len(mat[0]) - 1 ):
                    arr.append(mat[row][col])
                    row-=1
                    col+=1
                arr.append(mat[row][col])
                if(col == len(mat[0]) - 1):
                    row+=1
                else:
                    col+=1
                up = False
            else:
                while(row < len(mat) - 1 and col > 0):
                    arr.append(mat[row][col])
                    row+=1
                    col-=1
                arr.append(mat[row][col])

                if(row == len(mat) - 1):
                    col+=1
                else:   
                    row+=1
                up = True
        return arr
