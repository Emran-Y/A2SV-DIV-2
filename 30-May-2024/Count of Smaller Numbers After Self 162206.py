# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        result  = [0] * len(nums)                                   
        enum = list(enumerate(nums))                              
        
        self.mergeSort(enum, 0, len(nums) - 1, result)
        return result
    
    def mergeSort(self, enum, start, end, result):
        if start >= end: return
        
        mid = start + (end - start) // 2
        self.mergeSort(enum, start, mid, result)
        self.mergeSort(enum, mid + 1, end, result)
        self.merge(enum, start, mid, end, result)
    
    def merge(self, enum, start, mid, end, result):
        p, q = start, mid + 1
        inversion_count = 0                               
        temp = []
        
        while p <= mid and q <= end:
            if enum[p][1] <= enum[q][1]:
                temp.append(enum[p])
                result[enum[p][0]] += inversion_count               
                p += 1
            else:
                temp.append(enum[q])
                inversion_count += 1                             
                q += 1
        
        while p <= mid:
            temp.append(enum[p])
            result[enum[p][0]] += inversion_count                 
            p += 1
        
        while q <= end:         
            temp.append(enum[q])
            q += 1
        
        enum[start:end+1] = temp                               