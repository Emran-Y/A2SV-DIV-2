class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        v1 = 0
        if(start < destination):
            v1 = sum(distance[start:destination])
        elif(destination < start):
            v1 = sum(distance[destination:start])
        else:
            return 0
        return min(v1,sum(distance) - v1)
       


        


