class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxi = 0
        c = 0
        for i in range(len(flips)):
            maxi = max(maxi,flips[i])
            if(i+1==maxi):
                c+=1
        return c