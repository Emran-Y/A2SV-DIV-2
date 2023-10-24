class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while( r < len(prices)):
            if(prices[r] - prices[l] < 0):
                l = r
                r = r + 1
            else:
                maxP = max(maxP,prices[r] - prices[l])
                r+=1
        return maxP

        
