class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key = lambda point: (((point[0]) ** 2) + ((point[1]) ** 2)) ** 0.5)

        ans = []

        for i in range(k):
            ans.append(points[i])
        return ans