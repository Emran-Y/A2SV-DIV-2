class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        
        points.sort()
        _max = 0
        
        L = 0
        R = 1
        while(R < len(points)):
            _max = max(_max,points[R][0] - points[L][0])
            L+=1
            R+=1
        return _max
        
        