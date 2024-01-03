class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if(len(s) == 0):
            return 0
        max_num = 0

        g.sort()
        s.sort()

        left = 0
        right = 0

        while(right < len(s)):
            if(left >= len(g)):
                return max_num
            if s[right] >= g[left]:
                max_num += 1
                left+=1
                right+=1
            else:
                right+=1
        return max_num

      



        