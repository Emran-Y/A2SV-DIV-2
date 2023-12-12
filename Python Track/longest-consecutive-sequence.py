class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTable = {}

        for i in nums:
            hashTable[i] = 1

        maxi = 0

        for i in nums:
            if(i - 1 in hashTable):
                continue
            else:
                c = 0
                while(i in hashTable):
                    c+=1
                    i+=1
                maxi = max(maxi,c)
        return maxi

        
        
