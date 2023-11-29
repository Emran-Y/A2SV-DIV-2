class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x = n

        while( (x % 2 !=0) or (x%n) !=0):
            x+=1
        return x