class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            def power(x,n):
                if n == 1:
                    return x
                if n == 0:
                    return 1
                res = power(x,n//2)
                res = res * res
                if n%2!=0:
                    res = res * x

                return res
            return power(x,n)
        else:
            def power(x,n):
                if n == 0:
                    return 1
                if n == 1:
                    return (1 / x)
                
                res = power(x,n//2)
                res = res * res

                if n%2!=0:
                    res = (1 / x) * res
                
                return res
            return power(x,abs(n))