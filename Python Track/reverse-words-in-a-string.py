class Solution:
    def reverseWords(self, s: str) -> str:
        
        txt = ''

        temp = ''

        for i in s[::-1]:
            if(i==' ' and temp):
                txt+=temp[::-1] + ' '
                temp = ''
            elif(i!=' '):
                temp+=i
        if(temp):
            txt+=temp[::-1]
        ans = txt.strip()

        return ans

