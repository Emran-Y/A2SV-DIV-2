class Solution:
    def totalMoney(self, n: int) -> int:
        num_7 = 0

        if(n <= 7):
            num_7 = 1
        else:
            num_7 = n // 7 + 1
        
        tot = 0

        for i in range(num_7):
          temp = i + 1 
          for j in range(7):
            if(j + 1 <= n):
              tot += j + temp
          n-=7
        return tot
