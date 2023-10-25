class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        L = 0
        window = ''
        my = []
        p_count = {}
        window_count = {}
        for char in p:
            p_count[char] = 1 + p_count.get(char,0)
        for i in range(len(s)):
            if len(window) < len(p) - 1:
                window += s[i]
                window_count[s[i]] = 1 + window_count.get(s[i],0)
            else:
                window += s[i]
                window_count[s[i]] = 1 + window_count.get(s[i],0)
                if window_count == p_count:
                    my.append(L)
                window_count[s[L]] -=1
                if(window_count[s[L]] == 0):
                    window_count.pop(s[L]) 
                L += 1
                window = window[1:]
        return my
