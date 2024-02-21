class Solution:
    def countGoodNumbers(self, n: int) -> int: 
        def even(n):
            if n == 0:
                return 0
            if n == 1:
                return 5
            res = even(n//2)
            res = res * res
            if n%2!=0:
                res = res * 5
            res = res % (10**9 + 7)
            return res
        def odd(n):
            if n == 0:
                return 1
            if n == 1:
                return 4
            res = odd(n//2)
            res = res * res
            if n%2!=0:
                res = res * 4
            res = res % (10**9 + 7)
            return res

        return (even((n + 1) // 2) * odd(n//2)) % (10**9 + 7)