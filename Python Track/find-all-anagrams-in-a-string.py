class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left_tracker = 0
        answer = []
        p_count = {}
        window_count = {}
        for char in p:
            p_count[char] = 1 + p_count.get(char,0)
        for i in range(len(s)):
            if sum(window_count.values()) < len(p) - 1:
                window_count[s[i]] = 1 + window_count.get(s[i],0)
            else:
                window_count[s[i]] = 1 + window_count.get(s[i],0)
                if window_count == p_count:
                    answer.append(left_tracker)
                window_count[s[left_tracker]] -=1
                if(window_count[s[left_tracker]] == 0):
                    del window_count[s[left_tracker]] 
                left_tracker += 1
        return answer