class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L = 0
        total =0
        maxi = 0
        f_count = {}
        for i in range(len(fruits)):
            f_count[fruits[i]] = 1 + f_count.get(fruits[i],0)
            total +=1
            while(len(f_count) > 2):
                f = fruits[L]
                f_count[f] =  f_count.get(f,0) - 1
                L+=1
                total-=1
                if not f_count[f]:
                    f_count.pop(f)
            maxi = max(total,maxi)
        return maxi
