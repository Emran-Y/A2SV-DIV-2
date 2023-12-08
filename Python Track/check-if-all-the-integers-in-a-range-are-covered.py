class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range(left,right+1):
            flag = False
            for j in ranges:
                if( i in j or (j[0] <= i <= j[1])):
                    flag = True
            if(flag):
                continue
            else:
                return False
        return True