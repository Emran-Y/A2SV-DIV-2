class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ta = {}
        k = 0
        temp = 0
        for i in nums:
            ta[k] = i
            k+=1
            if(i%2==0):
                temp+=i
        
        answer = []
        for i in queries:
            if(ta[i[1]]%2!=0):

                ta[i[1]] = i[0] + ta[i[1]]
                if(ta[i[1]]%2==0):
                    temp += ta[i[1]]
                    answer.append(temp)
                else:
                    answer.append(temp)
            else:
                t = ta[i[1]]
                ta[i[1]] = i[0] + ta[i[1]]
                if(ta[i[1]]%2==0):
                    temp += ta[i[1]] - t
                    answer.append(temp)
                else:
                    temp-=t
                    answer.append(temp)

        return answer
