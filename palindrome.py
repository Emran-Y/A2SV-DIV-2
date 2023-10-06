import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha =  ''.join(c for c in s if c.isalnum() and c != '_')
        return alpha.upper() == alpha.upper()[::-1]
