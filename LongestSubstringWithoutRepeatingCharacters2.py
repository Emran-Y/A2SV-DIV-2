class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ''
        L = 0
        maxi = 0
        for i in range(len(s)):
            if s[i] not in window:
                window+=s[i]
            else:
                maxi = max(maxi,len(window))
                while(s[i] in window ):
                    window = window[L + 1:]
                window+=s[i]
        if(len(s) == 1):
            return 1
        else:
            return max(maxi,len(window))
