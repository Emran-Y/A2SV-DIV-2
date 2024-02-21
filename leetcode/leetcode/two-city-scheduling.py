class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        new_cost=sorted(costs, key=lambda x: x[0]-x[1])
        sum_ = 0
        for i in range(len(costs)//2):
            sum_+=new_cost[i][0]
        for i in range(len(costs)//2,len(costs)):
            sum_+=new_cost[i][1]
        return sum_


        