# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def helper(n):
            x=[]
            while n % 2 == 0:
                x.append(2)
                n = n / 2
            for i in range(3,int(math.sqrt(n))+1,2):
                while n % i== 0:
                    x.append(i)
                    n = n / i
            if n > 2:
                x.append(n)
            return sum(x)
        while(n!=helper(n)):
            n=helper(n)
        return int(n)            
              