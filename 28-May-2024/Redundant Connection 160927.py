# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=[i for i in range(len(edges))]
        last=[0,0]
        def find(x):
            while graph[x]!=x:
                x=graph[x]
            return x
        def union(x,y):
            rootx=find(x-1)
            rooty=find(y-1)
            graph[rooty]=rootx
        for i in edges:
            if find(i[0]-1)==find(i[1]-1):
                last=i
            else:
                union(i[0],i[1])
        return last