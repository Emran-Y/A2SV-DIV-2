class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        ta = {}

        k = 0
        for i in nums:
            ta[i] = k
            k+=1
        
        for i in operations:
            nums[ta[i[0]]] = i[1]
            ta[i[1]] = ta[i[0]]
        return nums