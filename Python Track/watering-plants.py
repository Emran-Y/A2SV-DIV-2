class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        tot = 0

        L = -1
        R = 0
        cap = capacity

        while(R<len(plants)): 
            if(plants[R] <= cap):
                tot+=1
                cap-=plants[R]
            if(R + 1 < len(plants) and plants[R + 1] <= cap):
                R+=1
            elif(R + 1 < len(plants) and plants[R+1] > cap):
                
                cap = capacity
                tot+= R - L
                tot += R - L 
                R+=1
            else:
                R+=1

        return tot
