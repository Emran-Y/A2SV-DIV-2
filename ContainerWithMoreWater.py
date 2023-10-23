class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxi = 0
        while(l < r):
            maxi = max((min(height[l],height[r]) * (r - l) ),maxi)
               
            if(height[l] <= height[r]):
                l+=1
            else:
                r-=1
        return maxi
