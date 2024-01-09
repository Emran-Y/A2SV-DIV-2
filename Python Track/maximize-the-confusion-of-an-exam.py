class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        

        ans = 0

        d = {'T':0,'F':0}

        l = 0

        for R in range(len(answerKey)):
            d[answerKey[R]]+=1

            while(d['T'] > k and d['F'] > k):
                d[answerKey[l]]-=1
                l+=1
            ans = max(ans,sum(d.values()))
            
        return ans