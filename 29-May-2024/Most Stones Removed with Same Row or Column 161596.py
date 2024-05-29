# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rank = [1] * n
        parent = [i for i in range(n)]
        
        def union(i, j):
            i, j = find(i), find(j)
            if i == j:
                return 0
            if rank[i] < rank[j]:
                i, j = j, i
            rank[i] += rank[j]
            parent[j] = parent[i]
            return 1
        
        def find(i):
            while i != parent[i]:
                parent[i] = i = parent[parent[i]]
            return i
        
        rows, cols = {}, {}
        removeds = 0
        for i, (row, col) in enumerate(stones):
            if row in rows:
                removeds += union(i, rows[row])
            else:
                rows[row] = i
            if col in cols:
                removeds += union(i, cols[col])
            else:
                cols[col] = i
        
        return removeds