class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if(len(people) == 0):
            return 1
        people.sort()

        l = 0
        r = len(people) - 1
        tot = 0
        while(r >= 0 and r >= l):
            if(r==l):
                tot+=1
                break
            if(people[l] + people[r] <= limit):
                tot+=1
                r-=1
                l+=1
            else:
                tot+=1
                r-=1
        return tot 
