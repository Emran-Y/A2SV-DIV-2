class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0]  * n for i in range(m)]
        
        set_guard = set(tuple(inner_array) for inner_array in guards)
        set_wall = set(tuple(inner_array) for inner_array in walls)
        dxn_d = [[1,0],[0,1],[-1,0],[0,-1]]

        for i in range(m):
            for j in range(n):
                if (i,j) in set_guard:
                    for dx,dy in dxn_d:
                        temp = [i,j]
                        while ( (temp[0] + dx < m and temp[0] + dx >= 0) and (temp[1] + dy < n and temp[1] + dy >= 0)  ):
                            temp[0]+=dx
                            temp[1]+=dy
                            if (temp[0],temp[1]) in set_guard or (temp[0],temp[1]) in set_wall:
                                break
                            else:
                                matrix[temp[0]][temp[1]] = 1

        c = 0

        for i in range(m):
            for j in range(n):
                if (i,j) in set_guard and (i,j) in set_wall:
                    continue
                else:
                    if matrix[i][j] == 1:
                        c+=1
        return (m * n) - (c + len(set_guard) + len(set_wall))

                                
