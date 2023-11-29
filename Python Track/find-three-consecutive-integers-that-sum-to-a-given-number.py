class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if(num%3==0):
            n = num/3 - 1
            return [int(n),int(n+1),int(n+2)]
        else:
            return []