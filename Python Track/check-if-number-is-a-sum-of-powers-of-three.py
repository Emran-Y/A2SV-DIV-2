class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        max_p = int(math.log(n, 3))
        temp = 0
        
        for i in range(max_p,-1,-1):
            temp+=3**i
            for j in range(max_p - 1, -1 ,-1):
                if (temp == n):
                    return True
                temp+=3**j
                if(temp == n):
                    return True
                if(temp > n):
                    temp-=3**j
            temp = 0
        return True if n == 1 else False