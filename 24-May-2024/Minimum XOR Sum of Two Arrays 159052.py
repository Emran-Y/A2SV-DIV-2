# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        precomputed = [[a[i] ^ b[j] for j in range(n)] for i in range(n)]
        cache = {}

        def dp(mask: int) -> int:
            if mask in cache:
                return cache[mask]
            i = bin(mask).count("1")
            if i >= n:
                return 0
            min_value = float('inf')
            for j in range(n):
                if mask & (1 << j) == 0:
                    min_value = min(min_value, precomputed[i][j] + dp(mask | (1 << j)))
            cache[mask] = min_value
            return min_value
        
        return dp(0)

