class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = [str(i) for i in digits]
        num = int(''.join(t))
        num+=1
        return [int(i) for i in str(num)]
    
        