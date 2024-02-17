class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p = list(palindrome)

        if len(palindrome) == 1:
            return ''
        
        for i in range(len(p)):
            if p[i] != 'a':
                p[i] = 'a'
                break
        if not p[::-1] == p:
            return ''.join(p)
        
        p = list(palindrome)

        for i in range(len(p) - 1,-1,-1):
            if p[i] == 'a':
                p[i] = 'b'
                break
        return ''.join(p)

