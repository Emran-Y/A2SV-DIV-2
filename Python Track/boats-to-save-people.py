class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        L = 0
        R = len(people) - 1
        mini = 0
        people.sort()
        while(R > L):
            if (people[R] + people[L] > limit):
                mini+=1
                R-=1
            else:
                mini+=1
                R-=1
                L+=1
        if(R == L):
            mini+=1
        return mini 