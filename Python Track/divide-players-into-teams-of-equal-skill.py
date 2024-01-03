class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if(len(skill) == 2):
            return skill[0] * skill[1]
        skill = sorted(skill)
        store = []
        l = 0
        r = len(skill) - 1
        temp = skill[0] + skill[r]
        while(r > 0 and r>l):
            if(skill[l] + skill[r] == temp):

                store.append([skill[l],skill[r]])
                l+=1
                r-=1
            else:
                return -1
        final = 0
        for i in store:
            final+=i[0] * i[1]
        return final

        