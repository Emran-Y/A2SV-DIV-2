class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0



        d = {}

        v = 0


        l = 0

        for R in range(len(s)):
            d[s[R]] = 1 + d.get(s[R],0)
            if(s[R] in {'a','e','i','o','u'}):
                v+=1

            while(sum(d.values()) > k):
                d[s[l]]-=1
                if(s[l] in {'a','e','i','o','u'}):
                    v-=1
                if(d[s[l]] == 0):
                    del d[s[l]]
                l+=1
            ans =  max(ans,v)
            

        return ans
