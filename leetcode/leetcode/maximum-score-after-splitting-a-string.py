class Solution:
    def maxScore(self, s: str) -> int:
        tot0 = s.count('0')
        tot1 = s.count('1')

        max_val = 0

        prefix_sum = []

        for i in s:
            prefix_sum.append(int(i))
        
        for i in range(1,len(s)):
            prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]
        
        for i in range(len(s) - 1 ):
            max_val = max(max_val,
                ((((i+1) - prefix_sum[i])) + ((tot1) - prefix_sum[i]) )
            )
        return max_val