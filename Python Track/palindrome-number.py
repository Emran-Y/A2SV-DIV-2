class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = 0
        temp = x
        while(x > 0):
            r = r * 10 + x%10
            x = x // 10
        return temp == r