class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        maxi = 0
        R = 0
        L = 0
        while(R < len(fruits)):
            if (len(dic) < 2 or fruits[R] in dic):
                dic[fruits[R]] = 1 + dic.get(fruits[R],0)
                R+=1
            else:
                maxi = max(maxi,sum(dic.values()))
                while(len(dic) == 2):
                    if dic[fruits[L]] == 1:
                        dic.pop(fruits[L])
                    else:
                        dic[fruits[L]] = dic.get(fruits[L]) - 1
                    L+=1
                dic[fruits[R]] = 1 + dic.get(fruits[R],0)
                R+=1
        return max(maxi,sum(dic.values()))

        

        