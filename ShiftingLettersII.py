class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        store = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        prifix = [0] * len(s)
        s = list(s)
        for i in shifts:
            if(i[2] == 1):
                prifix[i[0]] +=1
                if ( i[1] + 1 < len(prifix) ):
                    prifix[i[1] + 1] -=1
            else:
                prifix[i[0]] -=1
                if ( i[1] + 1 < len(prifix) ):
                    prifix[i[1] + 1] +=1
        prifix_sum = []
        for i in range(len(prifix)):
            if(i==0):
                prifix_sum.append(prifix[i])
            else:
                prifix_sum.append(prifix_sum[i - 1] + prifix[i])
        for i in range(len(prifix_sum)):
            if(prifix_sum[i] == 0):
                continue
            else:
                s[i] = store[(store.index(s[i]) + prifix_sum[i])%26]
        return ''.join(s)
