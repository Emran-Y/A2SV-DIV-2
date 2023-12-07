class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        table = {}

        for i in nums:
            table[i] = 1 + table.get(i,0)

        t = len(nums) // 3

        final = []
        for i in table:
            if(table[i] > t):
              final.append(i)
        return final