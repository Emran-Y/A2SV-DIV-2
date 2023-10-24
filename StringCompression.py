class Solution:
    def compress(self, chars: List[str]) -> int:
        if(len(chars)==1):
            return 1 
        l = 0
        r = 1
        s=''
        temp = 1
        while(r<len(chars)):
            if((chars[r] != chars[l]) and temp == 1):
                s+=chars[l]
                l+=1
                if(r + 1 >= len(chars)):
                    s+=chars[r]
                r+=1
            elif((chars[r] != chars[l]) and temp != 1):
                s+=chars[l]
                s+=str(temp)
                temp = 1
                l = r
                if(r + 1 >= len(chars)):
                    s+=chars[r] 
                r = r + 1
            elif(chars[r] == chars[l]):
                if(r + 1 >= len(chars)):
                    s+=chars[l]
                    s+=str(temp + 1)
                r+=1
                temp+=1
        
        p = 0
        for i in range(len(chars)):
            if(p < len(s)):
                chars[p] = s[p]
                p+=1
            else:
                chars.pop()
        return len(s)
