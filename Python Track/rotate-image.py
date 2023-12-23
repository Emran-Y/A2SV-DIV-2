class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            if(i >= len(matrix) - (i+1)):
                break
            matrix[i],matrix[len(matrix) - (i+1)] = matrix[len(matrix) - (i+1)],matrix[i]

        # table = {}

        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         table[f'{i} {j}'] = matrix[i][j]

        # print(table)

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                if(i==j):
                    continue
                else:
                    # print((j,i),table[f'{i} {j}'],(i,j))
                    # matrix[j][i] = table[f'{i} {j}']
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        