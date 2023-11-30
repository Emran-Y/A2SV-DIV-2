class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        dict = {}
        
        for i in nums:
            dict[i] = 1 + dict.get(i,0)
            
        final = 0
        
        for i in dict:
            if dict[i] >= 2:
                final+=( math.factorial(dict[i]) / (2 * math.factorial(dict[i] - 2)))
        return int(final)
    
       
        