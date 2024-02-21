class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(s,L = 0 ,R = len(s) - 1):
            if L >= R:
                return 
            s[L],s[R] = s[R],s[L]
            reverse(s,L + 1,R - 1)
        reverse(s,0,len(s) - 1)
        
            