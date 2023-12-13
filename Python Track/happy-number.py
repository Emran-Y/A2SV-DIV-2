class Solution:
    def isHappy(self, n: int) -> bool: 
        visited = set()
        while n != 1:
            digits = str(n)
            n = sum(int(digit) ** 2 for digit in digits)
            if n in visited:
                return False
            visited.add(n)
        return True