class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res_array = []
        for i in range(len(matrix[0])):
            temp =[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            res_array.append(temp)
        return res_array



