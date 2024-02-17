class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        num_of_arrows = 1
        start,end = points[0][0],points[0][1]

        for i in range(1,len(points)):
            if points[i][0] > start and points[i][0] > end:
                num_of_arrows += 1
                start,end = points[i][0],points[i][1]
            else:
                start,end = max(start,points[i][0]),min(end,points[i][1])
        return num_of_arrows
