class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for _ in s1:
            s1_count[_] = 1 + s1_count.get(_,0)
        s2_count = {}
        L = 0
        for R in range(len(s2)):
            if(R - L + 1 < len(s1)):
                s2_count[s2[R]] = 1 + s2_count.get(s2[R],0)
            else:
                s2_count[s2[R]] = 1 + s2_count.get(s2[R],0)
                if(s1_count == s2_count):
                    return True
                else:
                    if(s2_count.get(s2[L]) == 1):
                        s2_count.pop(s2[L])
                    else:
                        s2_count[s2[L]]-=1
                    L+=1
        return False
