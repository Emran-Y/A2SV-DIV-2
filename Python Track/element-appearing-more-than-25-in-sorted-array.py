class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashTable = {}
        for i in arr:
            hashTable[i] = 1 + hashTable.get(i,0)
    
        n = int(len(arr) * 0.25)
        for key,val in hashTable.items():
            if(val > n):
                return key