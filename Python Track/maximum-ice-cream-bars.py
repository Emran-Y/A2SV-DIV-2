class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        s_array = [0] * (max(costs) + 1)

        for i in costs:
            s_array[i]+=1
        
        k = 0
        for i in range(len(s_array)):
            for j in range(s_array[i]):
                costs[k] =  i
                k+=1
        max_ = 0

        for i in costs:
            if ( coins >= i ):
                max_+=1
                coins-=i
            else:
                break
        return max_
