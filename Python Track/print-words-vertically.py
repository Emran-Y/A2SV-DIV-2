class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = list(s.split())
        max_str = 0

        for  i in s_list:
            max_str = max(max_str,len(i))

        final_list = []

        k = 0
        for i in range(max_str):
            temp = ''
            for j in s_list:
                if(k < len(j)):
                    temp+=j[k]
                else:
                    temp+=' '
            final_list.append(temp.rstrip())
            temp = ''
            k+=1

        return final_list