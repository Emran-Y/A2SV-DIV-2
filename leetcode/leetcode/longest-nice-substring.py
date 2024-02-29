class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if s == '':
            return ''
        if len(s) == 1:
            return ''
        
        left = ''
        right = ''

        for i in range(len(s)):
            if s[i].isupper():
                if s[i].lower() not in s:
                    left = s[:i]
                    right = s[i+1:]
                    break
            else:
                if s[i].upper() not in s:
                    left = s[:i]
                    right = s[i+1:]
                    break
        if left == '' and right == '':
            return s
        left_ans = self.longestNiceSubstring(left)
        right_ans = self.longestNiceSubstring(right)

        if len(left_ans) >= len(right_ans):
            return left_ans
        else:
            return right_ans