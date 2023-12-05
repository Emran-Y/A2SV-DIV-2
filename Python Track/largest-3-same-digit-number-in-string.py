class Solution:
    def largestGoodInteger(self, num: str) -> str:
        final = ''
        L = 0

        while(L + 2 < len(num)):
            temp = num[L] + num[L+1] + num[L+2]
            if temp[0] == temp[1] and temp[0] == temp[2] and temp[1] == temp[2]:
                if(final == ''):
                    final = str(temp)
                else:
                    compare = max(int(temp),int(final))
                    final = str(compare)
            L+=1
        return final if final!='0' else '000'
